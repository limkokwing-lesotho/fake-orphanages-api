from flask import Flask
from flask_cors import CORS
import datetime
import data

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return data.all_houses


@app.route('/01')
def house_1():
    return data.house1


@app.route('/02')
def house_2():
    return data.house2


@app.route('/03')
def house_3():
    return data.house3


@app.route('/04')
def house_4():
    return data.house4


@app.route('/05')
def house_5():
    return data.house5


@app.route('/06')
def house_6():
    return data.house6


if __name__ == '__main__':
    app.run()
