from flask import Flask, jsonify, request, abort

import setting

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    list_of_thing = []
    for thing in setting.available_things:
        list_of_thing.append(thing.as_dict())
    return jsonify(list_of_thing)


@app.route('/<int:thing_id>/', methods=['PUT'])
def update_thing_data(thing_id):
    if not request.json:
        return {'iot_error': 'Not JSON.'}, 400
    thing = next((thing for thing in setting.available_things if thing.id == thing_id), None)
    if thing is None:
        return {'iot_error': 'Thing not found.'}, 404
    if thing.update(request.json):
        return jsonify(thing.data)
    else:
        return {'iot_error': 'Invalid data.'}, 400

@app.route('/on')
def turn_on():
    list_of_thing = []
    for thing in setting.available_things:
        thing.turn_on()
        list_of_thing.append(thing.as_dict())
    return jsonify(list_of_thing)


@app.route('/off')
def turn_off():
    list_of_thing = []
    for thing in setting.available_things:
        thing.turn_off()
        list_of_thing.append(thing.as_dict())
    return jsonify(list_of_thing)


app.run(host='0.0.0.0', debug=True)
