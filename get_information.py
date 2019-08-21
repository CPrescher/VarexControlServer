import requests
import time

server_address = 'http://131.169.215.66:5000'


def get_attribute(attribute):
    result = requests.get('{}/attribute/{}'.format(server_address, attribute))
    if result:
        try:
            return float(result.content)
        except ValueError:  # if it cannot be converted to a number
            return result.content
    else:
        return None


print(get_attribute('nFrames1'))
print(get_attribute('FileDir1'))
print(get_attribute('non_existent'))
print(get_attribute('ExposureTime1'))


t1 = time.time()
for _ in range(10):
    print(get_attribute('nFrames1'), 'Time needed: {}'.format(time.time() - t1))
    t1 = time.time()

print()

t1 = time.time()
time_array = []
for _ in range(30):
    get_attribute('nFrames1')
    time_array.append(time.time() - t1)
    t1 = time.time()

print(time_array)
