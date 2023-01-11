from sqlalchemy import ForeignKeyConstraint
from . import db
from datetime import datetime

class Material(db.Model):
    __tablename__='materials'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}\n"
        str = str.format( self.id, self.name, self.description)
        return str

class Shape(db.Model):
    __tablename__='shapes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}\n"
        str = str.format( self.id, self.name, self.description)
        return str

class Glasses(db.Model):
    __tablename__='glasses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Float, nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
    shape_id = db.Column(db.Integer, db.ForeignKey('shapes.id'))
    eyesize = db.Column(db.Integer, nullable=False)
    bridgesize = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    lateststyle = db.Column(db.Boolean, nullable=False)
    image = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        str = "Id: {}, Name: {}, Gender: {}, Price: {}, Material: {}, Shape: {}, Eye-size: {}, Bridge-size: {}, Description: {}, Latest Style: {}, Image: {}\n" 
        str =str.format( self.id, self.name,self.gender,self.price, self.material_id, self.shape_id, self.eyesize, self.bridgesize, self.description, self.lateststyle, self.image)
        return str

orderdetails = db.Table('orderdetails',
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'),nullable=False),
    db.Column('glasses_id', db.Integer,db.ForeignKey('glasses.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'glasses_id')
)

class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    address_street = db.Column(db.String(32))
    address_city = db.Column(db.String(32))
    address_postcode = db.Column(db.String(32))
    date = db.Column(db.DateTime)
    glasses = db.relationship("Glasses", secondary=orderdetails, backref="orders")
    totalcost = db.Column(db.Float)
    
    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Street Address: {}, City: {}, Post Code: {}, Date: {}, Glasses: {}, Total Cost: {}\n" 
        str =str.format( self.id, self.status,self.firstname,self.surname, self.email,self.phone, self.address_street, self.address_city, self.address_postcode, self.date, self.glasses, self.totalcost)
        return str