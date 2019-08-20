from flask import Flask, request
import PyTango
import tango

app = Flask(__name__)

device = "tango://131.169.215.66:10000/hibef/Varex/1"
varex = PyTango.DeviceProxy(device)


@app.route('/status')
def status():
    try:
        return str(varex.state())
    except:
        return None


@app.route('/StartAcq/<det>')
def start_acquisition(det):
    if status() == "ON":
        varex.command_inout("StartAcq{}".format(det))
        return "Collection started", 200
    return 'Detector is not ready for commands', 412


@app.route('/StopAcq/<det>')
def stop_acquisition(det):
    if status() == "MOVING":
        varex.command_inout("StopAcq{}".format(det))
        return "Collection stopped", 200
    return 'Detector is not collecting', 412


@app.route('/attribute', methods=['POST'])
def set_param():
    if status() == "ON":
        try:
            attribute_info = varex.attribute_query(request.form['attribute'])
        except tango.DevFailed:
            return "Attribute {} does not exist".format(request.form['attribute']), 400

        if "d" in attribute_info.format or "f" in attribute_info.format:
            try:
                value = float(request.form['value'])
            except ValueError:
                return "Value format is incorrect", 400
        else:
            value = request.form['value']

        varex.write_attribute(request.form['attribute'], value)
        return "Attribute {} has been set to {}".format(request.form['attribute'], value)
    return 'Detector is not ready for commands', 412


if __name__ == '__main__':
    app.run()
