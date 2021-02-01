import csv
import datetime

from flask import make_response

from app import db
from app.models import Device


def check_file_name(uploaded_file):
    if uploaded_file.filename == '':
        return make_response({"error": "Incorrect file name"}, 400)

    if str(str(uploaded_file).split('.')[-1][:3]).split('.')[-1] != 'csv':
        return make_response(
            {"error": "Incorrect file format, required format is .csv"},
            400
        )


def check_file_content(row, row_data, key_list):
    for key, value in row_data.items():
        if value == '':
            return make_response(
                {"error": "Incorrect file structure"}, 400
            )

    for r in row:
        if r not in key_list:
            return make_response(
                {"error": "Incorrect file structure"}, 400
            )


def check_or_create(row):
    date_time_obj = datetime.datetime.strptime(
        str(row['Time']), '%Y-%m-%d %H:%M:%S'
    )

    device_test_obj = Device.query.filter_by(
        device_type=row['Device type'],
        operator=row['Operator'],
        time=date_time_obj,
        success=int(row['Success'])
    ).first()

    if device_test_obj is not None:
        pass

    if device_test_obj is None:
        device_test = Device(
            device_type=row['Device type'],
            operator=row['Operator'],
            time=date_time_obj,
            success=int(row['Success'])
        )
        db.session.add(device_test)
        db.session.commit()


def file_parser(uploaded_file, key_list):
    decoded_file = uploaded_file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)

    for row in reader:
        row_data = dict(row)
        cfc = check_file_content(row, row_data, key_list)
        if cfc is not None:
            return cfc

        check_or_create(row)


def get_stat(device_test):
    result = dict()

    for dt in device_test:
        if dt.device_type in result:
            result[dt.device_type]['all_tests'] += 1
            if dt.success == 0:
                result[dt.device_type]['success_tests'] += 1
            if dt.success == 1:
                result[dt.device_type]['failed_tests'] += 1

        else:
            result[dt.device_type] = dict()
            result[dt.device_type]['all_tests'] = 1
            if dt.success == 0:
                result[dt.device_type]['success_tests'] = 1
                result[dt.device_type]['failed_tests'] = 0
            if dt.success == 1:
                result[dt.device_type]['failed_tests'] = 1
                result[dt.device_type]['success_tests'] = 0

    return result
