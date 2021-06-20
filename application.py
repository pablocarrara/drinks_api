# https://www.youtube.com/watch?v=qbLc5a9jdXo&ab_channel=CalebCurryCalebCurry
# DESDE LOS 28 MINUTUTOS EMPIEZA EL DESARROLLO DE LA REST API
# REST API SERVER DE BEBIDAS(B)
# DESDE LOS 28 MINUTOS BREVE EXPLICACION DE COMO CREAR UN AMBIENTE VIRTUAL CON LAS DEPENDENCIAS DE MIS APPs

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key = True) # id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} - {self.description}'


@app.route('/')
def index():
    return 'Hello'


@app.route('/api/drinks')
def get_drinks():
    output = []
    drinks = Drink.query.all()

    for drink in drinks:
        drink_data = {"name" : drink.name, "description" : drink.description, "id" : drink.id}
        output.append(drink_data)

    return {'drinks' : output}


@app.route('/api/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name" : drink.name, "description" : drink.description}


@app.route('/api/drinks', methods = ['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()

    return {'id' : drink.id}


@app.route('/api/drinks/<id>', methods = ['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error" : "not found"}
    db.session.delete(drink)
    db.session.commit()

    return {"message" : "deleted ok!"}
