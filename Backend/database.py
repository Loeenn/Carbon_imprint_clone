import pyodbc
import bcrypt


# main part------------------------------------------------------------------------------------------
def connect_db():
    server = 'tcp:176.99.158.202'
    database = 'Carbon_imprint'
    username = 'guest_carbon'
    password = 'asskarramba'
    cnxn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}',
        ansi=True)
    return cnxn.cursor()


# air-----------------------------------------------------------------------------------------------air


# reil----------------------------------------------------------------------------------------------reil


# auto-----------------------------------------------------------------------------------------------auto


# water-----------------------------------------------------------------------------------------------water


# site ----------------------------------------------------------------------------------------------site


def checkEmail(email):
    cursor = connect_db()
    cursor.execute('''
            SELECT * from Users 
            WHERE email = ?
                   ''', email)
    return bool(cursor.fetchone())


def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password.encode('utf8'), bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password.encode('utf8'), hashed_password.encode('utf8'))


def addUser(email, first_name, password):
    cursor = connect_db()
    password_hash = get_hashed_password(password)
    if checkEmail(email):
        return -1
    cursor.execute('''
        INSERT INTO USERS(email, first_name, password_hash)
        VALUES(?, ?, ?)
        
               ''', email, first_name, password_hash)
    cursor.commit()
    return 1


def get_user_hash(email):
    cursor = connect_db()
    cursor.execute('''
            SELECT password_hash
            from Users
            where email = ?
        ''', email)
    password_hash = cursor.fetchone()[0]
    return password_hash
