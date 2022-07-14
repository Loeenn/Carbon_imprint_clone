import pyodbc

def connect_db():
    server = 'tcp:176.99.158.202'
    database = 'Carbon_imprint'
    username = 'guest'
    password = 'asskarramba'
    cnxn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}',
        ansi=True)
    return cnxn.cursor()