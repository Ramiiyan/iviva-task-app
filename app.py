from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
import requests

app = Flask(__name__)
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
    for obj in response:
        equip_list.append(Equipment(obj["AssetCategoryID"], obj["AssetID"], obj["__rowid__"], obj["OperationalStatus"]))

    print(Equipment.device_count)
    print(Equipment.operational_device_count)

    return jsonify({
        "Status": "Success",
        "code": 200,
        "device_count": Equipment.device_count,
        "operational_device_count": Equipment.operational_device_count,
        "data": EquipmentSchema(many=True).dump(equip_list)
    })


def retrieve_data(total_data, max_per_request):
    res = []
    # total_data = total_data + 1
    for limit in range(0, total_data, max_per_request):
        params = {"apikey": "SC:demo:64a9aa122143a5db", "max": max_per_request, "last": limit}
        response = requests.get('http://ivivaanywhere.ivivacloud.com/api/Asset/Asset/All', params=params)
        res = res + response.json()

    return res
