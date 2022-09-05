import math
from xlrd import open_workbook
import openrouteservice as ors
from openrouteservice.directions import directions
from openrouteservice.elevation import elevation_line
from openrouteservice.convert import decode_polyline
from geopy import Nominatim
import csv
import geopy.distance
from Backend.air_imprint import *
from Backend.database import connect_db


def brutto(m, volume):
    m = m
    volume = float(volume)
    quantity_cars = max(math.ceil(volume/120), math.ceil(m/69))
    print(quantity_cars * 23 + m)
    return quantity_cars * 23 + m


def insert_table(filename: str):
    book = open_workbook(f'C:\\Users\\egors\\Desktop\\{filename}.xls', on_demand=True)
    sheet = book.sheet_by_name('Sheet1')
    data = [[cell.value for cell in row] for row in sheet][1:]
    cursor = connect_db()
    print(data)
    for row in data[1:]:
        cursor.execute('''
            insert into
            Section_norms(
                start_station,
                end_station,
                electronic, 
                diesel, 
                length
            )
            values (?, ?, ?, ?, ?)
        ''', (str(row[4]).strip(), str(row[5]).strip(), row[2], row[3], row[-1]))
    cursor.commit()


def get_route_norm(start_station: str, end_station: str, km_tons: float) -> list[float, float]:
    fuel = [0, 0]
    cursor = connect_db()
    cursor.execute('''
        SELECT Stations_inbetween
        from Routs
        where Start_station = ?
        and End_station = ?
    ''', start_station, end_station)

    stations = cursor.fetchone()[0].split(', ')

    length = 0

    for i in range(1, len(stations)):
        cursor.execute('''
            SELECT Electronic, Diesel, Length
            from Section_norms
            where Start_station = ?
            and End_station = ?
        ''', stations[i - 1], stations[i])
        norms = cursor.fetchone()
        print(norms)
        fuel[0] += norms[0]*((km_tons * norms[2])/10000)
        fuel[1] += norms[1]*((km_tons * norms[2])/10000)
        length += norms[2]
    print(fuel, length)
    return [fuel, length]


def truck_imprint(start_point, end_point, length, weight):
    ors_key = '5b3ce3597851110001cf6248c07606351b6749d5a4de08dd46d57af2'
    client = ors.Client(key=ors_key)
    geolocator = Nominatim(user_agent="myApp")

    start_location = geolocator.geocode(f'Железнодорожная станция {start_point}')
    end_location = geolocator.geocode(f'Железнодорожная станция {end_point}')

    routes = directions(client, ((start_location.longitude, start_location.latitude),
                                 (end_location.longitude, end_location.latitude)), profile='driving-car', elevation=True)
    elevation_perc = routes['routes'][0]['summary']['ascent']/routes['routes'][0]['summary']['descent']

    imprint = weight/20*40*elevation_perc*(length/100)/1000*2.172
    return imprint


def oxygen_imprint(fuel: list) -> float:
    return round(fuel[0]*(3.581/4)*0.18 + fuel[0]*(1.603/10)*0.46 + fuel[1]*2.172)  # тонны углеродного следа


def translate(string: str) -> str:
    translator = {65: 1040, 66: 1042, 67: 1057, 69: 1045, 78: 1048, 75: 1050, 77: 1052, 72: 1053, 79: 1054, 80: 1056,
                  84: 1058, 88: 1061}
    translated = ''

    for i in range(len(string)):
        print(string[i], ord(string[i]))
        if ord(string[i]) not in range(1040, 1072) and ord(string[i]) not in (44, 45, 41, 40, 32, 49, 50, 51, 52, 53,
                                                                              54, 55, 56, 57, 48, 95, 46):
            translated += chr(translator[ord(string[i])])
        else:
            translated += string[i]

    return translated


def translate_routs() -> None:
    cursor = connect_db()
    for i in cursor.fetchall():
        cursor.execute('''
            update Routs
            set Start_station = ?,
            End_station = ?,
            Stations_inbetween = ?
            where Stations_inbetween = ?
        ''', translate(i[0]), translate(i[1]), translate(i[2]), i[2])
        cursor.commit()


# def translate_section_norms() -> None:
#     cursor = connect_db()
#     cursor.execute('select Section from Section_norms')
#     for item in cursor.fetchall():
#         cursor.execute('''
#             update Section_norms
#             set Section = ?
#             where Section = ?
#         ''', translate(item[0]), item[0])
#     cursor.commit()


def get_stations():
    cursor = connect_db()
    cursor.execute('''
        select Start_station
        from Section_norms
    ''')
    stations = list(dict.fromkeys([s[0] for s in cursor.fetchall()]))
    return stations


if __name__ == '__main__':
    print(get_air_imprint_by_model("KAMOV KA 32",get_airport_distance("Churchill Airport","Lake Monroe Seaplane Base"),10000,300),"кг CO2")