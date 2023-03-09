from flask import Flask, render_template, request, redirect, url_for, flash

from src.dao.professor import Professor
import os


app = Flask(__name__)

app.secret_key = os.urandom(12).hex()


@app.route('/')
def open_index():
    prof = Professor()
    lista = prof.get_professor_name()
    if len(lista) > 0:
        return render_template('index.html', lista= lista)
    else:
        flash('Arquivo Inválido!!!')
        return render_template('index.html')
    

@app.route('/', methods=['POST'])
def index():
    prof = Professor()
    id = request.form['id']
    return render_template('relatorio.html', prof = prof.get_data(int(id)))

@app.route('/search', methods=['POST'])
def search():
    txt = request.files['file']
    print("Esta aqui", txt.content_type)
    prof = Professor()
    prof.search_bd(txt)    

    return redirect(url_for('open_index'))


app.run(debug=True)