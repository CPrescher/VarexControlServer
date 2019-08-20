import PyTango
import sys, time


device = "tango://localhost:10000/hibef/Varex/1"

print("Connecting to Device")
varex = PyTango.DeviceProxy(device)
time.sleep(0.1)
print("Varex state: {}".format(varex.state()))

varex.write_attribute("FileDir1", "tcp://localhost:1234")
varex.write_attribute("ExposureTime1", 1)

varex.write_attribute("nFrames1", 1)
varex.write_attribute("Trigger1", 0)

time.sleep(0.1)

print("Collect Images")
varex.command_inout("StartAcq1")