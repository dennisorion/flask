from flask import Flask, jsonify, request
from markupsafe import escape

app2 = Flask(__name__)

usuarios = [
    {
        'nome': "Dennis",
        'idade': 31,
        'profissao': "psicologo",
    },
    {
        'nome': "Amanda",
        'idade': 37,
        'profissao': "pedagoga",
    },
    {
        'nome': "Rosa",
        'idade': 93,
        'profissao': "aposentada"
    ,}
    ]

@app2.route('/')
def main():
    return "olá"

@app2.route('/cadastro')
def cadastro():
    return "aqui fica teu currículo"

@app2.route('/abominacao')
def abominacao():
    return '<h1> minha primeira pagina </h1>' 

@app2.route('/bd')
def bd():
    return "<p1> Aqui fuca o banco de dados</p1>"

@app2.route('/formulario')
def formulario():

        form = '''
        <form>
            <label>Primeira nome:</label)
            <input type="text"><br><br>
            <label>idade:</label>
            <input type="text"><br><br>
            <input type="submit" value="enviar"
        </form>
'''
        return form

@app2.route('/v1/user/idade/<nome>', methods=["GET"])
def consulta(nome):
     for usuario in usuarios:
          if usuario ['nome'] == nome:
               return jsonify(idade=usuario['idade'])
     return jsonify(idade="usuario não encontrado"), 404

@app2.route('/v2/user/consulta/', methods=['GET'])
def consulta_usuario():
    nome = request.args.get('nome')
    profissao = request.args.get('profissao')
    for usuario in usuarios:
        if usuario ['nome'] == nome or usuario['profissao'] == profissao:
            return jsonify(usuario)
    return jsonify(mensagem='usuario não encontrao'), 404
               
if __name__ == "__main__":
    app2.run(debug=True)
