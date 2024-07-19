from flask import Flask, jsonify, request
from markupsafe import escape

app2 = Flask(__name__)


usuarios = [
    {
        'nome': "Amanda",
        'idade': 37,
        'profissao': "psi",
    },
    {
        'nome': 'Dennis',
        'idade': 31,
        'profissao': 'pedagogo',
    }
]

app2.route('/main')
def main():
    return '<h1>Ai sim porra</h1>'



if __name__ == "__main__":
    app2.run(debug=True)

