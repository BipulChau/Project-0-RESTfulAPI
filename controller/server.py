from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return "Welcome to MyBank : Fast, Friendly & Accurate Service", 200


@app.route('/api/customers/', methods=['GET', 'POST', 'PUT'])
def customers():
    return {}, 200


if __name__ == "__main__":
    app.run(debug=True, port=3132)
