from flask import Flask,jsonify,request

from db_setup import create_table, save_data_inicial
from db_manager import select_all_tarifas, select_one_tarifa, insert_one_tarifa
from clase_tarifa import Tarifa
from call_api_de_tercero import get_xr

app = Flask(__name__)

create_table()

# Home: Bienvenida a Parque Nacional Los Glaciares!
@app.get('/')
def home():
    return 'Bienvenido a Parque Nacional Los Glaciares!'


@app.get('/api/carga_inicial')
def carga_inicial():
    save_data_inicial()
    return 'Data inicial cargado!'


@app.route('/api/glaciares/tarifas', methods = ['GET'])
def get_all_tarifas():
    tarifas_list = select_all_tarifas()
    return jsonify([tarifa.serialize() for tarifa in tarifas_list])


@app.route('/api/glaciares/precios', methods = ['POST'])
def do_post():
    data = request.get_json()

    id = data['id']
    tarifa = data['tarifa']
    precio = data['precio']
    precio_2 = data['precio_2']

    obj_tarifa = Tarifa(id, tarifa, precio, precio_2)

    insert_one_tarifa(obj_tarifa)

    return jsonify(obj_tarifa.serialize())
@app.route('/api/glaciares/tarifas/usd/<tarifa_id>', methods = ['GET'])
def get_prenda_by_id_usd(tarifa_id):
    tarifa = select_one_tarifa(tarifa_id)
    xr = get_xr()
    print(tarifa)
    price_usd = tarifa['precio'] / xr
    tarifa['precio_dolares'] = round(price_usd, 2)
    return jsonify(tarifa)




if __name__ == '__main__':
    app.run()

