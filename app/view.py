from flask import request, jsonify, make_response
from flask_restful import Resource

from app.service import check_file_name, file_parser, get_stat
from app.models import Device
from app import db

import datetime


class UploadFileView(Resource):
    def post(self):
        uploaded_file = request.files['file']
        key_list = ['Device type', 'Operator', 'Time', 'Success']

        cfn = check_file_name(uploaded_file)
        if cfn is not None:
            return cfn

        parser = file_parser(uploaded_file, key_list)
        if parser is not None:
            return parser

        return make_response(jsonify({"result": "Successfully loaded"}), 200)


class DeviceStatView(Resource):
    def get(self):
        operator = request.args.get('operator')

        if operator is not None:
            device_test = Device.query.filter_by(operator=operator).all()

            return make_response(
                jsonify({"result": get_stat(device_test)}), 200
            )

        device_test = Device.query.all()
        return make_response(jsonify({"result": get_stat(device_test)}), 200)


class DeviceAddView(Resource):
    def post(self):
        data = request.json
        date_time = datetime.datetime.strptime(
            str(data['time']), '%Y-%m-%d %H:%M:%S'
        )
        device_test = Device(
            device_type=data['device_type'],
            operator=data['operator'],
            time=date_time,
            success=int(data['success'])
        )
        db.session.add(device_test)
        db.session.commit()

        return make_response(
            jsonify({"result": {"Device ID": device_test.id}}), 200
        )


class DeviceDeleteView(Resource):
    def delete(self, device_test_id):
        device_test = Device.query.filter_by(id=device_test_id).first()

        if device_test is None:
            return make_response(jsonify({"result": "Not found"}), 400)

        db.session.delete(device_test)
        db.session.commit()
        return make_response(jsonify({"result": "Successfully deleted"}), 200)
