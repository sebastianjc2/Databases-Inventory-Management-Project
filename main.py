from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from Backend.handler.parts import PartHandler
from Backend.handler.suppliers import SupplierHandler

app = Flask(__name__)

# apply CORS
CORS(app)


@app.route('/') # default route handler
def greeting():
    return 'Hello, this is the parts DB app practice'


# route to get all parts or add a part
@app.route('/parts', methods=['GET', 'POST'])
def getAllParts():
    if request.method == "GET":
        return PartHandler().getAllParts()
    elif request.method == "POST":  # performs insert queries
        data = request.json
        return PartHandler().insertPart(data)
    else:
        return jsonify('Not supported'), 405


# route to find a specific part
@app.route('/parts/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def searchPartByID(pid):
    if request.method == "GET":  # performs select-project-join queries
        return PartHandler().searchByID(pid)
    elif request.method == "PUT":  # performs update queries
        data = request.json
        return PartHandler().updateByID(pid, data)
    elif request.method == "DELETE":  # performs delete queries
        return PartHandler().deleteByID(pid)
    else:
        return jsonify('Not supported'), 405


@app.route('/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == "GET":
        return SupplierHandler().getAllSuppliers()
    elif request.method == "POST":  # performs insert queries
        data = request.json
        return SupplierHandler().insertSupplier(data)
    else:
        return jsonify('Not supported'), 405

@app.route('/suppliers/<int:sid>', methods=['GET', 'PUT', 'DELETE'])
def searchSupplierByID(sid):
    if request.method == "GET":  # performs select-project-join queries
        return SupplierHandler().searchByID(sid)
    elif request.method == "PUT":  # performs update queries
        data = request.json
        return SupplierHandler().updateByID(sid, data)
    elif request.method == "DELETE":  # performs delete queries
        return SupplierHandler().deleteByID(sid)
    else:
        return jsonify('Not supported'), 405


if __name__ == '__main__':
    app.run(debug=True)
