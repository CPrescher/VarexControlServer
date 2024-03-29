from flask import Flask, request
import PyTango
import tango

app = Flask(__name__)

device = "tango://0.0.0.0:10000/hibef/Varex/1"
varex = PyTango.DeviceProxy(device)


@app.route('/status')
def status():
    try:
        return str(varex.state())
    except:
        return None

@app.route('/StartAcq/<det>')
def start_acquisition(det):
    varex.command_inout("StartAcq{}".format(det))
    return "Collection started", 200


@app.route('/StopAcq/<det>')
def stop_acquisition(det):
    varex.command_inout("StopAcq{}".format(det))
    return "Collection stopped", 200

@app.route('/AllStartAcq')
def start_acquisition_all():
    varex.command_inout("AllStartAcq")
    return "Collection started", 200

@app.route('/AllStopAcq')
def stop_acquisition_all():
    varex.command_inout("AllStopAcq")
    return "Collection stopped", 200

@app.route('/attribute', methods=['POST'])
def set_attribute():
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


@app.route('/attribute/<attribute_name>')
def get_attribute(attribute_name):
    try:
        return str(varex.read_attribute(attribute_name).value), 200
    except tango.DevFailed:
        return "Attribute {} does not exist".format(request.form['attribute']), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0")
