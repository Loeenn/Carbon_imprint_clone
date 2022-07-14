import csv
import geopy.distance
from bs4 import BeautifulSoup as bs
import requests
from database import connect_db


def put_csv():
    data = []
    q = '''
            INSERT INTO airports(airport_id,
            ident,
            name,
            latitude_deg,
            longitude_deg,
            elevation_ft,
            continent,
            iso_country,
            iso_region,
            municipaly,
            gps_code,
            local_code
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''
    cursor = connect_db()
    cursor.fast_executemany = True
    with open('airports.csv', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile)
        i = 0
        for row in spamreader:
            if row[6] != '':
                if i == 5000:
                    print('ass')
                    cursor.executemany(q, data)
                    cursor.commit()
                    data = []
                    i = 0
                data.append((int(row[0]), row[1], row[3], float(row[4]), float(row[5]), int(row[6]), row[7], row[8],
                            row[9], row[10], row[12], row[14]))
                i += 1
        cursor.executemany(q, data)
        cursor.commit()

def get_airport_distance(departure_airport,arrival_airport):
    cursor = connect_db()
    departure_latitude=float(cursor.execute('''
    select latitude_deg from airports 
    where name = ?''',departure_airport).fetchone()[0])

    departure_longitude =float(cursor.execute('''
    select longitude_deg from airports 
    where name = ?''',departure_airport).fetchone()[0])

    arrival_latitude = float(cursor.execute('''
        select latitude_deg from airports 
        where name = ?''', arrival_airport).fetchone()[0])

    arrival_longitude = float(cursor.execute('''
        select longitude_deg from airports 
        where name = ?''', arrival_airport).fetchone()[0])

    coordinates_departure = (departure_latitude,departure_longitude)

    coordinates_arrival = (arrival_latitude,arrival_longitude)

    return geopy.distance.geodesic(coordinates_departure, coordinates_arrival).km


def average_airport_imprint(distance):
    return distance*0.621371*53*0.4535923


def average_air_imprint_by_kg(mass,distance):#масса в тоннах,среднее перевозмиое число берем из расчета того что самый популярный самолет имеет груозоподъёмность 18 тонн
    return (mass/18)*distance


def get_air_imprint_by_model(model,distance,cargo_weight,cargo_volume):
    cursor = connect_db()
    cursor.execute('''select load_volume from airplanes where airplane_name = ?''',[model])
    volume_airplane = int(cursor.fetchone()[0])
    cursor.execute('''select load_weight from airplanes where airplane_name = ?''',[model])
    weight_airplane =int(cursor.fetchone()[0])
    return (cargo_weight/weight_airplane)*(cargo_volume/volume_airplane)*distance*0.621371*53*0.4535923


def parse_airplane(url):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    name1 = soup.find('div',class_ = 'col lg_span_8 md_span_8 sm_span_6').find_all("h1")[0].text
    name = ' '.join(name1.split())
    value = soup.find('div',class_ = 'promo-item no-print')
    obiem=int(value.find_all("p")[0].text.split()[0])
    try:
        kruiz_speed =int(value.find_all("p")[1].text.split()[0])
    except:
        kruiz_speed = 0
    try:

        zagruzka = int(value.find_all("p")[3].text.split()[0])
    except:
        zagruzka = 20000
    try:
        razmer_uderzhania =value.find_all("p")[4].text.split()[0].split("x")
    except:
        razmer_uderzhania = 0
    try:
        razmer_uderzhania_lenght = int(razmer_uderzhania[0])
    except:
        razmer_uderzhania_lenght = 0
    try:
        razmer_uderzhania_width = int(razmer_uderzhania[1])
    except:
        razmer_uderzhania_width = 0
    try:
        razmer_uderzhania_height = int(razmer_uderzhania[2])
    except:
        razmer_uderzhania_height=0
    try:
        razmer_dveri = value.find_all("p")[5].text.split()[0].split("x")
    except:
        razmer_dveri=0
    try:
        razmer_dveri_width = int(razmer_dveri[0])
    except:
        razmer_dveri_width=0
    try:
        razmer_dveri_height = int(razmer_dveri[1])
    except:
        razmer_dveri_height=0
    try:
        ibzhii_obiem_nagruzki = int(value.find_all("p")[6].text.split()[0])
    except:
        ibzhii_obiem_nagruzki = 0
    try:
        maximum_diapazon = int(value.find_all("p")[7].text.split()[0])
    except:
        maximum_diapazon=0
    return [obiem,kruiz_speed,zagruzka,razmer_uderzhania_lenght,razmer_uderzhania_width,razmer_uderzhania_height,
            razmer_dveri_width,razmer_dveri_height,ibzhii_obiem_nagruzki,maximum_diapazon,name]

def add_airplane(table):
    cursor = connect_db()
    values = parse_airplane('https://www.aircharter.ru'+table)
    print(values)
    cursor.execute('''
    INSERT INTO airplanes (load_volume,cruise_speed,load_weight,holding_length,holding_width,holding_height,door_width,door_height,whole_volume_load,max_range_km,airplane_name)
    values (?,?,?,?,?,?,?,?,?,?,?)''',[values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10]])
    cursor.commit()

def readP():
        with open("airs", "r") as f:

            contents = f.read()

            soup = bs(contents, 'lxml')
            act = soup.find_all("div", class_="aircraft-teaser zoom list-item")
            for i in act:
                act1 = i.find("a")
                yield act1["href"]


if __name__ == '__main__':
    print(get_air_imprint_by_model("KAMOV KA 32",get_airport_distance("Churchill Airport","Lake Monroe Seaplane Base"),10000,300),"кг CO2")