from flask import Flask

app=Flask(__name__)

@app.route('/darOla/')
def saudacao():
    return 'Olá Mundo!\nJoao Guilherme'

if __name__=='__main__':
    app.run(debug=True)