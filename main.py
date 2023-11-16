from flask import Flask, jsonify, request
from flask_cors import CORS
from Backend import dbconfig as config
# Import handlers
from Backend.handler.parts import PartHandler
from Backend.handler.suppliers import SupplierHandler
from Backend.handler.customer import CustomerHandler
from Backend.handler.racks import RackHandler
from Backend.handler.incomingnTransaction import IncomingTransactionHandler

# App initialization
app = Flask(__name__)
app.config.from_object(config)
CORS(app)


@app.route('/')  # default route handler
def greeting():
    return 'Hello, this is the parts DB app practice'


# route to get all parts or add a part
@app.route('/sqlytes/parts', methods=['GET', 'POST'])
def getAllParts():
    if request.method == "GET":
        return PartHandler().getAllParts()
    elif request.method == "POST":  # performs insert queries
        data = request.json
        return PartHandler().insertPart(data)
    else:
        return jsonify('Not supported'), 405


# route to find a specific part
@app.route('/sqlytes/parts/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
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


@app.route('/sqlytes/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == "GET":
        return SupplierHandler().getAllSuppliers()
    elif request.method == "POST":  # performs insert queries
        data = request.json
        return SupplierHandler().insertSupplier(data)
    else:
        return jsonify('Not supported'), 405


@app.route('/sqlytes/suppliers/<int:sid>', methods=['GET', 'PUT', 'DELETE'])
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



@app.route("/sqlytes/customer", methods=["POST", "GET"])
def allCustomers():
    if request.method == "POST":
        data = request.json
        return CustomerHandler().addCustomer(data)
    elif request.method == "GET":
        return CustomerHandler().getAllCustomers()
    else:
        return jsonify("Not supported"), 405


@app.route("/sqlytes/customer/<int:cid>", methods=["GET", "PUT", "DELETE"])
def customerById(cid):
    if request.method == "GET":
        return CustomerHandler().getCustomerById(cid)
    elif request.method == "PUT":
        data = request.json
        return CustomerHandler().modifyCustomerById(cid, data)
    elif request.method == "DELETE":
        return CustomerHandler().deleteCustomerById(cid)
    else:
        return jsonify("Not supported"), 405


@app.route("/sqlytes/rack", methods=["POST", "GET"])
def allRacks():
    if request.method == "POST":
        data = request.json
        return RackHandler().addRack(data)
    elif request.method == "GET":
        return RackHandler().getAllRacks()
    else:
        return jsonify("Not supported"), 405


@app.route("/sqlytes/rack/<int:rid>", methods=["GET", "PUT", "DELETE"])
def rackById(rid):
    if request.method == "GET":
        return RackHandler().getRackByID(rid)
    elif request.method == "PUT":
        data = request.json
        return RackHandler().updateByID(rid, data)
    elif request.method == "DELETE":
        return RackHandler().deleteByID(rid)
    else:
        return jsonify("Not supported"), 405



@app.route("/sqlytes/incomingTransaction", methods=["POST", "GET"])
def allIncomingTransactions():
    if request.method == "POST":
        data = request.json
        return IncomingTransactionHandler().addIncomingTransaction(data)
    elif request.method == "GET":
        return IncomingTransactionHandler().getAllIncomingTransaction()
    else:
        return jsonify("Not supported"), 405


@app.route("/sqlytes/incomingTransaction/<int:itid>", methods=["GET", "PUT"])
def incomingTransactionById(itid):
    if request.method == "GET":
        return IncomingTransactionHandler().getIncomingTransactionById(itid)
    elif request.method == "PUT":
        data = request.json
        return IncomingTransactionHandler().modifyIncomingTransactionByID(itid, data)
    else:
        return jsonify("Not supported"), 405


if __name__ == '__main__':
    app.run(debug=True)
