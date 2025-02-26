from iniciar import db, migrate

class Pessoas(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String,nullable=True)
    idade=db.Column(db.Integer,nullable=True)
    peso=db.Column(db.Float,nullable=True)
    jogofav=db.Column(db.String,nullable=True)
