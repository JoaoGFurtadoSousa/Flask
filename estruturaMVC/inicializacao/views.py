from inicializacao import app 
from flask import render_template,url_for


@app.route('/')
def olaMundo():
    return render_template('index.html')

@app.route('/for/')
def urldinamica():
    return '''<h1>Fez do jeito certo e está funcionando</h1>'''

app.route('/quebra')
def assimquebra():
    return 'Testando'

@app.route('/chamandouser/')
def exibeusuario():
    nome='Joao Guilherme'
    return f'''<h1>Olá {nome}!</h1>'''

'''@app.route('/userdeformaotimizada')
def exibirUsuarioOtimizado():
    nome='Joao Guilherme'
    return render_template('saudarUser.html',nome=nome)
'''

@app.route('/userdeformaotimizada')
def exibirUsuarioOtimizado():
    dicionario={'nome':'Joao Guilherme',
                'idade':19,
                'Profissão':'Programador Backend Python'}
    return render_template('saudarUser.html',dicionario=dicionario)