import PyTango


device = "tango://131.169.215.66:10000/hibef/Varex/1"
varex = PyTango.DeviceProxy(device)


attribute_info = varex.attribute_query('ExposureTime1')
print(attribute_info.format)

print(attribute_info.format % 30.20)