from iniciar import app,db
from flask import render_template, request
from iniciar.model import Pessoas

@app.route('/', methods=['GET','POST'])
def ola():
    dicionario={}
    if request.method=='GET':
        pesquisado=request.args.get('pesquisa')
        dicionario.update({'resultado':pesquisado})
        print(dicionario['resultado']) 
    if request.method=='POST':
        envia=request.form['enviaDados']
        print(envia)
    return render_template('index.html',dicionario=dicionario)



@app.route('/salvar/',methods=['GET','POST'])
def salvar():
    if request.method=='POST':
        nome=request.form['nome']
        idade=request.form['idade']
        peso=request.form['peso']
        jogofav=request.form['jogofav']

        pessoa1=Pessoas(nome=nome,
                        idade=idade,
                        peso=peso,
                        jogofav=jogofav)
        
        db.session.add(pessoa1)
        db.session.commit()
    return render_template('conecta.html')
