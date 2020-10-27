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
        abort(400)
    thing = next((thing for thing in setting.available_things if thing.id == thing_id), None)
    if thing is None:
        abort(404)
    if thing.update(request.json):
        return thing.data
    else:
        abort(400)


app.run(host='0.0.0.0', debug=True)
