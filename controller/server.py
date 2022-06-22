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
def profile(customer_id):
    return "Get customer with an id, if the customer exists", 200


if __name__ == "__main__":
    app.run(debug=True, port=3132)
