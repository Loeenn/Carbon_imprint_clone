import math, pyodbc
from xlrd import open_workbook


def connect_db():
    server = 'tcp:176.99.158.202'
    database = 'Carbon_imprint'
    username = 'guest'
    password = 'karramba'
    cnxn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}',
        ansi=True)
    return cnxn.cursor()


def brutto(m, volume):
    m = float(m)
    volume = float(volume)
    quantity_cars = max(math.ceil(V/120), math.ceil(m/69000))
    return quantity_cars * 23000 + m


def insert_table(filename: str):
    book = open_workbook(f'C:\\Users\\egors\\Desktop\\{filename}.xls', on_demand=True)
    sheet = book.sheet_by_name('Sheet1')
    data = [[cell.value for cell in row] for row in sheet][1:]
    cursor = connect_db()
    for row in data:
        cursor.execute('''
            insert into
            Section_norms(
                Section,
                Electronic,
                Disel
            )
            values (?, ?, ?)
        ''', (str(row[0]), row[1], row[2]))
    cursor.commit()


insert_table('ВС Т отчет по участкам обслуживания')


