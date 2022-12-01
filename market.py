from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Float(), nullable=False)
    code = db.Column(db.String(length=16), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'USB HUB 3.0 Ethernet adapter mrežni RJ45 Gigabit LOGILINK UA0173A', 'code': '40639',
         'price': 55,
         'link': 'https://electronic.ba/proizvod/40639/usb-hub-30-ethernet-adapter-mrezni-rj45-gigabit-logilink-ua0173a'},
        {'id': 2, 'name': '(Intenso) USB Flash drive 8GB Hi-Speed USB 2.0, Rainbow Line, ZELENI - USB2.0-8GB/Rainbow',
         'code': '4500', 'price': 13.50},
        {'id': 3, 'name': 'SWITCH CISCO CBS220 24-Port Gigabit', 'code': '21022168', 'price': 599.01,
         'link': 'https://www.plus.ba/bs/product/63974/switch-cisco-cbs220-24-port-gigabit'}
    ]
    return render_template('market.html', items=items)
