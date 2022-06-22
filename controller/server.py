from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return "Welcome to MyBank : Fast, Friendly & Accurate Service", 200


@app.route('/customers/')
def customers():
    return "Gets all customers", 200


@app.route('/customers/', methods=['POST'])
def customers():
    return "Creates a new customer", 201


@app.route('/customer/<customer_id>')
def customer(customer_id):
    return "Get customer with an id, if the customer exists", 200


@app.route('/customer/<customer_id>', methods = ['PUT'])
def customer_id(customer_id):
    return "Update customer with an id, if the customer exists"


if __name__ == "__main__":
    app.run(debug=True, port=3132)
