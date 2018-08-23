from app import db

class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    foodName = db.Column(db.String(100),unique=True)
    foodNum  = db.Column(db.Int(10), unique=True)

    def __init__(self, foodName, foodNum):
        self.foodName  = foodName
        self.foodNum = foodNum
    def __repr__(self):
        return '<foodName %r>' % self.foodName
