# # from flask import Flask
# # from markupsafe import escape

# # app = Flask(__name__)

# # @app.route('/')
# # def ola():
# #     return '<h1> Minha primeira pagina </h1>'

# # @app.route('algo/')
# # def segundapagina():
# #     return '<p1> Esta é minha primeira pagina </p1>'

# # from flask import Flask

# # app = Flask(__name__)

# # @app.route('/')
# # def primeiraPagina():
# #     return "<h1> Minha página </h1>"


# # @app.route('/segunda_pagina')
# # def segunda_pagina():
# #     return "<h1> segunda página </h1>"


# # if __name__ == "__main__":
# #     app.run(debug=True)

# alunos = [
#     {
#         "nome": "Dennis",
#         "idade": 31,
    
#     }
# ]

from flask import Flask,jsonify,request

app = Flask(__name__)

usuarios = [

    {
        'nome': "Amanda", 
        'email': "xxxxx", 
        'idade': 32
     },
    {
        'nome': "Eduardo", 
        'email': "xxxxxddddf", 
        'idade': 56
    },
    {
        'nome': "benfica", 
        'email': "xxxxxdddddsdfdfef", 
        'idade': 56
    ,}
    ]

@app.route('/')
def primeiraPagina():
    return "<h1> Minha página </h1>"


@app.route('/segunda_pagina')
def segunda_pagina():
    return "<h1> segunda página </h1>"

@app.route('/formulario')
def formulario():

    form = '''
    <form>
        <label>Primeiro nome:</label>
        <input type="text"><br><br>
        <label>Segundo nome:</label>
        <input type="text"><br><br>
        <input type="submit" value="enviar">
    </form>
'''
    return form

@app.route('/cadastro')
def cadastro():
    return "dennis, 31 anos"

@app.route('/cadastro_json')
def cadastro_json():
    return jsonify(nome="Dennis orion", idade=31)


@app.route('/v1/user/idade/<nome>', methods=['GET'])
def retorna_idade(nome):
    if nome == "dennis":
        return jsonify(idade=31)
    else:
        return jsonify(idade="não encontrado")

@app.route('/v2/user/idade/<nome>', methods=['GET'])
def consulta(nome):
    for usuario in usuarios:
        if usuario ['nome'] == nome:
            return jsonify(idade=usuario['idade'])
        
    return jsonify(idade="usuario não encontrado"), 404

@app.route('v3/user/consulta/', methods=['GET'])
def consulta_usuario():
    nome = request.args.get('nome')
    email = request.args.get('email')
    for usuario in usuarios:
        if usuario ['nome'] == nome or usuario['email'] == email:
            return jsonify(usuario)
    return jsonify(mensagem='não encontrado'), 404

if __name__ == "__main__":
    app.run(debug=True)


