import sqlite3
DATABASE_NAME= 'LosGlaciares.db'
from clase_tarifa import Tarifa

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn
def create_table():
    my_query = """CREATE TABLE IF NOT EXISTS Tarifas (
                id TEXT PRIMARY KEY,
                tarifa TEXT NOT NULL,
                precio INTEGER NOT NULL,
                precio_2 INTEGER NOT NULL
                 )
            """

    db = get_db()
    cursor = db.cursor()
    cursor.execute(my_query)
def save_data_inicial():

    tarifa_data = [
        Tarifa('T01', 'Tarifa General', 12000, 6000),
        Tarifa('T02', 'Residentes nacionales', 2500, 1250),
        Tarifa('T03', 'Niños y niñas de 6 a 16 años', 1500, 750),
        Tarifa('T04', 'Residentes provinciales', 1000, 500),
        Tarifa('T05', 'Jubilados, Niños hasta 5 años,Personas con Discapacidad', 0, 0),
    ]

    db = get_db()
    cursor = db.cursor()

    for obj in tarifa_data:
        statement = """INSERT OR IGNORE INTO Tarifas (id, tarifa, precio, precio_2) 
                                               VALUES (?, ?, ?, ? )"""
        cursor.execute(statement, [obj.id, obj.tarifa, obj.precio, obj.precio_2])


    db.commit()
    db.close()

