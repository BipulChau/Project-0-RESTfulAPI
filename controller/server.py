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
    return "Creates a new customer", 200


@app.route('/customer/<customer_name>')
def profile(customer_name):
    return "Profile of individual customer appears here", 200


if __name__ == "__main__":
    app.run(debug=True, port=3132)
