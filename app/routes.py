from app import api
from app.view import UploadFileView, DeviceStatView, DeviceAddView, \
    DeviceDeleteView


api.add_resource(UploadFileView, '/api_v1/upload')
api.add_resource(DeviceStatView, '/api_v1/stat')
api.add_resource(DeviceAddView, '/api_v1/test_result')
api.add_resource(DeviceDeleteView, '/api_v1/test_result/<int:device_test_id>')

