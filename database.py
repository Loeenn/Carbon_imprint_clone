import pyodbc


#main part------------------------------------------------------------------------------------------
def connect_db():
    server = 'tcp:176.99.158.202'
    database = 'Carbon_imprint'
    username = 'guest'
    password = 'asskarramba'
    cnxn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}',
        ansi=True)
    return cnxn.cursor()


def headers(table):
    cursor = connect_db()
    cursor.execute(f""" SELECT * FROM {table}
                """)
    return [columnName[0] for columnName in cursor.description]

def selectTop20(table):
    cursor = connect_db()
    cursor.execute(f""" SELECT TOP 20 *
                           FROM {table}
               """)
    print(headers(table))
    for i in cursor.fetchall():
        print([str(j) for j in i])

#air-----------------------------------------------------------------------------------------------air



#reil----------------------------------------------------------------------------------------------reil


#auto-----------------------------------------------------------------------------------------------auto



#water-----------------------------------------------------------------------------------------------water







# site ----------------------------------------------------------------------------------------------site


def createUserTable():
    cursor = connect_db()
    if not cursor.tables(table='Users', tableType='TABLE').fetchone():
        cursor.execute('''
        CREATE TABLE Users(
        id int IDENTITY NOT NULL PRIMARY KEY,
        email varchar(128),
        first_name varchar(128),
        password_hash varchar(256)
        );
               ''')
        cursor.commit()


def dropUserTable():
    if input("do you sure to DROP User TABLE?(y/n)").rstrip().lower() == 'y':
        cursor = connect_db()
        cursor.execute('DROP TABLE Users')
        cursor.commit()


def checkEmail(email):
    cursor = connect_db()
    cursor.execute('''
            SELECT * from Users 
            WHERE email = ?
                   ''', email)
    return bool(cursor.fetchone())



def addUser(email, first_name, password_hash):
    cursor = connect_db()
    if checkEmail(email):
        return -1
    cursor.execute('''
        INSERT INTO USERS(email, first_name, password_hash)
        VALUES(?, ?, ?)
        
               ''', email, first_name, password_hash)
    cursor.commit()
    return 1

def delitUser(email):
    cursor = connect_db()
    cursor.execute('''
                    DELETE FROM Users 
                    WHERE email = ?
                   ''', email)
    cursor.commit()


def userId(email):
    cursor = connect_db()
    cursor.execute('''
                SELECT id
                from Users
                where email = ?
            ''', email)
    user_id = cursor.fetchone()[0]
    return user_id



def userHash(email):
    cursor = connect_db()
    cursor.execute('''
            SELECT password_hash
            from Users
            where email = ?
        ''', email)
    password_hash = cursor.fetchone()[0]
    return password_hash

def getUserById(id):
    cursor = connect_db()
    cursor.execute('''
            SELECT *
            from Users
            where id = ?
        ''', id)
    data = dict(zip(headers("Users"), cursor.fetchone()))
    return data


# dropUserTable()
# createUserTable()
# print(headers('Users'))
# print(checkEmail('esly@gm.r'))
# addUser("admin@admin.admin", "ADMIN", 'pbkdf2:sha256:260000$3zrTXmv325HhYoWO$57d497a4ab613f9a9ff501909b46d67609fdb61004e8d0ed8b84132a1da43de6')
# selectTop20('Users')