from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def ola():
    return '<h1> Minha primeira pagina </h1>'

@app.route('algo/')
def segundapagina():
    return '<p1> Esta é minha primeira pagina </p1>'
