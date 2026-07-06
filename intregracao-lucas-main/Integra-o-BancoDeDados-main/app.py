# Import do framework flask
# Import do render_template para ler o HTML e busca ou o endereço do arquivo ou a URL
# request para capturar os dados
from flask import Flask, render_template, request

import mysql.connector 

# Para vincular as páginas e saberem ond estão:

app = Flask(__name__)

# Cria conexão com o mySQL
bd_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1',
    'ssl_disabled': True
}

# Criação de rota para o arquivo HTML principal

@app.route('/cadastrar', methods=['POST'])
def indexRota():
    return render_template('index.html')

def criar_cadastro():
    try:

        cpf = request.form['cpf']
        primeiro_nome=request.form['primeiro_nome']
        sobrenome = request.form['sobrenome']
        idade = request.form['idade']

        conectar =  mysql.connector.connect(**bd_config)

        curso = conectar.cursor()

        query ="INSERT INTO cliente1 (CPF, PRIMEIRO_NOME, SOBRENOME, IDADE) VALUES(%s,%s,%s,%s,%s)"
        curso.execute(query,(cpf,primeiro_nome,sobrenome,idade))


        conectar.commit()

        curso.close()

        conectar.close()

        return f"<h3> cliente {primeiro_nome} gravado com sucesso! </h3> <a href ='/'> volta </a>"
    except mysql.connector.Error as err:
        return f"erro ao gravar no banco:{err}"
    

   
# Biblioteca mysql.connector conecta o Python com o MySQL
#