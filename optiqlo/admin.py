from flask import Blueprint
from . import db
from .models import Glasses, Shape, Material
import datetime

bp = Blueprint('admin',__name__,url_prefix='/admin/')

@bp.route('/dbseed/')
def dbseed():
    
    material1=Material(id=1, name='Acetate', description='A lightweight material', image='acetate.jpg')
    material2=Material(id=2, name='Metal', description='A heavy-duty material', image='metal.jpg')
    material3=Material(id=3, name='Titanium', description='A strong durable material', image='titanium.jpg')
    try:
         db.session.add(material1)
         db.session.add(material2)
         db.session.add(material3)
         db.session.commit()
    except:
        return 'There was an issue adding the materials in dbseed function'
    
    shape1=Shape(id=1, name='Rectangular', description='Square them up', image='rectangular.jpg')
    shape2=Shape(id=2, name='Round', description='Never too curvy', image='round.jpg')
    shape3=Shape(id=3, name='Cats Eye', description='A classy touch for the feminine', image='catseye.jpg')
    shape4=Shape(id=4, name='Aviator', description='Howard Hughes watch out', image='aviator.jpg')

    try:
         db.session.add(shape1)
         db.session.add(shape2)
         db.session.add(shape3)
         db.session.add(shape4)
         db.session.commit()
    except:
        return 'There was an issue adding the shapes in dbseed function'
    
    frame1 = Glasses(id='1', name='Frame 1', gender='Unisex', price=59.99, material_id=material1.id, shape_id=shape2.id, eyesize=52, bridgesize=20, \
        description='An awesome number 1 frame', lateststyle=False, image='frame1.jpg')
    frame2 = Glasses(id='2', name='Frame 2', gender='Female', price=59.99, material_id=material1.id, shape_id=shape3.id, eyesize=53, bridgesize=19,\
        description='An awesome number 2 frame', lateststyle=False, image='frame2.jpg')
    frame3 = Glasses(id='3', name='Frame 3', gender='Male', price=59.99, material_id=material3.id, shape_id=shape4.id, eyesize=56, bridgesize=18,\
        description='An awesome number 3 frame', lateststyle=False, image='frame3.jpg')
    frame4 = Glasses(id='4', name='Frame 4', gender='Unisex', price=59.99, material_id=material2.id, shape_id=shape1.id, eyesize=55, bridgesize=16,\
        description='An awesome number 4 frame', lateststyle=False, image='frame4.jpg')
    frame5 = Glasses(id='5', name='Frame 5', gender='Male', price=59.99, material_id=material1.id, shape_id=shape4.id, eyesize=55, bridgesize=18,\
        description='An awesome number 5 frame', lateststyle=False, image='frame5.jpg')
    frame6 = Glasses(id='6', name='Frame 6', gender='Unisex', price=69.99, material_id=material2.id, shape_id=shape2.id, eyesize=49, bridgesize=19,\
        description='An awesome number 6 frame', lateststyle=False ,image='frame6.jpg')
    frame7 = Glasses(id='7', name='Frame 7', gender='Female', price=69.99, material_id=material2.id, shape_id=shape3.id, eyesize=51, bridgesize=20,\
        description='An awesome number 7 frame', lateststyle=False, image='frame7.jpg')
    frame8 = Glasses(id='8', name='Frame 8', gender='Male', price=69.99, material_id=material2.id, shape_id=shape2.id, eyesize=52, bridgesize=19,\
        description='An awesome number 8 frame', lateststyle=False, image='frame8.jpg')
    frame9 = Glasses(id='9', name='Frame 9', gender='Male', price=69.99, material_id=material1.id, shape_id=shape4.id, eyesize=52, bridgesize=18,\
        description='An awesome number 9 frame', lateststyle=False, image='frame9.jpg')
    frame10 = Glasses(id='10', name='Frame 10', gender='Unisex', price=89.99, material_id=material1.id, shape_id=shape2.id, eyesize=51, bridgesize=21,\
        description='An awesome number 10 frame', lateststyle=False, image='frame10.jpg')
    frame11 = Glasses(id='11', name='Frame 11', gender='Unisex', price=89.99, material_id=material1.id, shape_id=shape2.id, eyesize=52, bridgesize=20,\
        description='An awesome number 11 frame', lateststyle=False, image='frame11.jpg')
    frame12 = Glasses(id='12', name='Frame 12', gender='Unisex', price=89.99, material_id=material3.id, shape_id=shape2.id, eyesize=51, bridgesize=22,\
        description='An awesome number 12 frame', lateststyle=False, image='frame12.jpg')
    frame13 = Glasses(id='13', name='Frame 13', gender='Male', price=89.99, material_id=material1.id, shape_id=shape1.id, eyesize=53, bridgesize=19,\
        description='An awesome number 13 frame', lateststyle=True, image='frame13.jpg')
    frame14 = Glasses(id='14', name='Frame 14', gender='Female', price=99.99, material_id=material2.id, shape_id=shape1.id, eyesize=54, bridgesize=18,\
        description='An awesome number 14 frame', lateststyle=True, image='frame14.jpg')
    frame15 = Glasses(id='15', name='Frame 15', gender='Male', price=99.99, material_id=material3.id, shape_id=shape2.id, eyesize=50, bridgesize=17,\
        description='An awesome number 15 frame', lateststyle=True, image='frame15.jpg')
    frame16 = Glasses(id='16', name='Frame 16', gender='Female', price=99.99, material_id=material1.id, shape_id=shape3.id, eyesize=50, bridgesize=19,\
        description='An awesome number 16 frame', lateststyle=True, image='frame16.jpg')
    frame17 = Glasses(id='17', name='Frame 17', gender='Female', price=99.99, material_id=material1.id, shape_id=shape2.id, eyesize=50, bridgesize=116,\
        description='An awesome number 17 frame', lateststyle=True, image='frame17.jpg')

    try:
        db.session.add(frame1)
        db.session.add(frame2)
        db.session.add(frame3)
        db.session.add(frame4)
        db.session.add(frame5)
        db.session.add(frame6)
        db.session.add(frame7)
        db.session.add(frame8)
        db.session.add(frame9)
        db.session.add(frame10)
        db.session.add(frame11)
        db.session.add(frame12)
        db.session.add(frame13)
        db.session.add(frame14)
        db.session.add(frame15)
        db.session.add(frame16)
        db.session.add(frame17)
        db.session.commit()
    except:
        return 'There was an issue adding the frames in dbseed function'

    return 'Data loaded'

    
