from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from dao.professor import Professor
import os


app = Flask(__name__)

app.secret_key = os.urandom(12).hex()

bootstrap = Bootstrap5(app)


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
    print(txt.content_type)
    prof = Professor()
    prof.search_bd(txt)    

    return redirect(url_for('open_index'))

if __name__ == '__main__':
    app.run(debug=True)