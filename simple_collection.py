import requests

#server_address = 'http://127.0.0.1:5000'
server_address = 'http://131.169.215.66:5000'


def set_attribute(attribute, value):
    requests.post('{}/attribute'.format(server_address),
                  data={'attribute': attribute, 'value': value})


def collect_data():
    requests.get('{}/StartAcq/1'.format(server_address))


set_attribute('nFrames1', 30)
set_attribute('ExposureTime1', 3)
set_attribute('FileDir1', 'D:\\temp_images')
set_attribute('FileIndex1', 1)
collect_data()
