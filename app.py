import os
import psycopg2
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/quartos/', methods=['GET', 'POST'])
def quartos():
    # Abre uma conexão com o banco de dados
    connection = psycopg2.connect(os.getenv('DATABASE_URL'))
    cursor = connection.cursor()

    if request.method == 'POST':
        # Lê dados passados via requisição
        dados = request.get_json()

        # Valida os dados
        try:
            campos_faltantes = set(['andar', 'numero', 'quantidade_camas', 'tem_frigobar', 'categoria']) - set(dados.keys())
            assert not campos_faltantes
        except AssertionError:
            return {'campos_faltantes': list(campos_faltantes)}, 400

        # Insere dados recebidos no banco de dados
        cursor.execute('''
            INSERT INTO quartos (andar, numero, quantidade_camas, tem_frigobar, categoria)
            VALUES (%s, %s, %s, %s, %s)
        ''', (
            dados['andar'],
            dados['numero'],
            dados['quantidade_camas'],
            dados['tem_frigobar'],
            dados['categoria'],
        ))
        connection.commit()
        connection.close()

        return dados, 201

    if request.method == 'GET':
        cursor.execute('''
            SELECT id, andar, numero, quantidade_camas, tem_frigobar, categoria
            FROM quartos
        ''')

        quartos = []
        for id, andar, numero, quantidade_camas, tem_frigobar, categoria in cursor.fetchall():
            quartos.append({
                'id': id,
                'andar': andar,
                'numero': numero,
                'quantidade_camas': quantidade_camas,
                'tem_frigobar': tem_frigobar,
                'categoria': categoria,
            })
        connection.close()

        return {'quartos': quartos}, 200


@app.route('/hospedes/')
def hospedes():
    return 'alô xuxa'


@app.route('/reservas/')
def reservas():
    return 'alô xuxa'
