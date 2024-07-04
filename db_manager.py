import sqlite3
from clase_tarifa import Tarifa

DATABASE_NAME='LosGlaciares.db'

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def select_all_tarifas():

    db = get_db()
    cursor = db.cursor()

    query = "SELECT id, tarifa, precio, precio_2 FROM Tarifas "
    cursor.execute(query)
    list_rta = cursor.fetchall()

    tarifas_list = []
    for row in list_rta:
        id = row[0]
        tarifa = row[1]
        precio = row[2]
        precio_2 = row[3]

        obj_tarifa = Tarifa(id, tarifa, precio, precio_2)
        tarifas_list.append(obj_tarifa)

    db.close()


    return tarifas_list


def select_one_tarifa(tarifa_id):
    db = get_db()
    cursor = db.cursor()

    query = "SELECT id, tarifa, precio, precio_2 FROM Tarifas WHERE id =  '" + tarifa_id + "'"
    cursor.execute(query)

    row = cursor.fetchone()
    if row == None:
        return []

    id = row[0]
    tarifa = row[1]
    precio = row[2]
    precio_2 = row[3]
    obj_tarifa = Tarifa(id, tarifa, precio, precio_2)

    db.close()

    return obj_tarifa


def insert_one_tarifa(obj_tarifa):
    db = get_db()
    cursor = db.cursor()

    obj = obj_tarifa

    statement = """INSERT OR IGNORE INTO Tarifas (id, tarifa, precio, precio_2) 
                                               VALUES (?, ?, ?, ? )"""
    cursor.execute(statement, [obj.id, obj.tarifa, obj.precio, obj.precio_2])

    db.commit()
    db.close()