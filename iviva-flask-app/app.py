from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)

from models.EquipmentModel import Equipment, EquipmentSchema


@app.route("/")
def serve_me():
    return "Flask Server Working well."


@app.route("/retrieve_data")
def retrieve_data():
    equip_list = []
    total_data = request.args.get('total_data')
    max_per_req = request.args.get('max_per_req')

    response = retrieve_data(total_data=int(total_data), max_per_request=int(max_per_req))
    operational_device = 0
    for obj in response:
        equipment = Equipment
        equip_list.append(equipment(obj["AssetCategoryID"], obj["AssetID"], obj["__rowid__"], obj["OperationalStatus"]))
    Equipment.device_count = len(equip_list)
    print(Equipment.device_count)
    print(Equipment.count_operational(equip_list))
    # print(graph_data(equip_list))

    return jsonify({
        "Status": "Success",
        "code": 200,
        "device_count": Equipment.device_count,
        "operational_device_count": Equipment.operational_device_count,
        "equip_data": EquipmentSchema(many=True).dump(equip_list),
        "graph_data": graph_data(equip_list)
    })


def retrieve_data(total_data, max_per_request):
    res = []
    # total_data = total_data + 1
    for limit in range(0, total_data, max_per_request):
        params = {"apikey": "SC:demo:64a9aa122143a5db", "max": max_per_request, "last": limit}
        response = requests.get('http://ivivaanywhere.ivivacloud.com/api/Asset/Asset/All', params=params)
        res = res + response.json()

    return res


def graph_data(obj_list):
    equips = {}
    for obj in obj_list:
        if obj.asset_category_id not in equips:
            equips[obj.asset_category_id] = 1
        else:
            equips[obj.asset_category_id] = equips[obj.asset_category_id] + 1
    return equips


if __name__ == '__main__':
    app.run(debug=True)