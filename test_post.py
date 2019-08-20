import requests

requests.post('http://127.0.0.1:5000/attribute', data={'attribute': 'nFrames1', 'value': 2})
requests.post('http://127.0.0.1:5000/attribute', data={'attribute': 'FileDir1', 'value': "D:\\tpoer"})

requests.post('http://127.0.0.1:5000/attribute', data={'attribute': 'ExposureTime1', 'value': 3.123})
