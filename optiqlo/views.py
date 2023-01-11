from turtle import shape
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Glasses, Shape, Material, Order
from datetime import datetime, timedelta
from .forms import CheckoutForm, FriendSend, Help
from . import db
from sqlalchemy import desc

bp = Blueprint('main', __name__)

# Home Page Displaying All Products
@bp.route('/')
def index():
    query = request.args.get('query')
    if query:
        glasses = Glasses.query.filter(Glasses.name.contains(query) | Glasses.description.contains(query)) 
    else:
        glasses = Glasses.query.order_by(Glasses.id).all()
    return render_template('index.html', glasses = glasses, title='cool products') 

@bp.route('/priceascending/')
def ascending():
    glasses = Glasses.query.order_by(Glasses.price).all()
    return render_template('index.html', glasses = glasses, title='cool products') 

@bp.route('/pricedescending/')
def descending():
    glasses = Glasses.query.order_by(desc(Glasses.price)).all()
    return render_template('index.html', glasses = glasses, title='cool products') 

# Display Product Detail
@bp.route('/product/<productname>')
def product(productname):
    glasses = Glasses.query.filter(Glasses.name == productname)
    #material = Material.query.filter(Material.id == materialid)
    #shape = Shape.query.filter(Shape.id == shapeid)
    return render_template('product.html', glasses = glasses)

# Search by Shape Type
@bp.route('/shapes/')
def shapes():
    shapes = Shape.query.order_by(Shape.id).all()
    return render_template('shapes.html', shapes = shapes)

# Search by Shape Category
@bp.route('/shapes/glasses/<int:shapeid>')
def shapesglasses(shapeid):
    glasses = Glasses.query.filter(Glasses.shape_id == shapeid)
    return render_template('productview.html', glasses = glasses, title='interesting shapes')

# Search by Material Type
@bp.route('/materials/')
def materials():
    materials = Material.query.order_by(Material.id).all()
    return render_template('materials.html', materials = materials)

# Search by Material Category
@bp.route('/materials/glasses/<int:materialid>')
def materialsglasses(materialid):
    glasses = Glasses.query.filter(Glasses.material_id == materialid)
    return render_template('productview.html', glasses = glasses, title='exotic materials')

# Search by Male Category
@bp.route('/male/')
def male():
    glasses = Glasses.query.filter(Glasses.gender == 'Male')
    return render_template('productview.html', glasses = glasses, title='male styles')

# Search by Female Category
@bp.route('/female/')
def female():
    glasses = Glasses.query.filter(Glasses.gender == 'Female')
    return render_template('productview.html', glasses = glasses, title='female styles')

# Search by Unisex Category
@bp.route('/unisex/')
def unisex():
    glasses = Glasses.query.filter(Glasses.gender == 'Unisex')
    return render_template('productview.html', glasses = glasses, title='unisex styles')

# Search by Latest Styles Category
@bp.route('/lateststyles/')
def lateststyles():
    glasses = Glasses.query.filter(Glasses.lateststyle == True)
    return render_template('productview.html', glasses = glasses, title='latest styles')

# Contact Us
@bp.route('/contact/')
def contact():
    return render_template('info.html', info = 'Contact Us')

# Pricing
@bp.route('/pricing/')
def pricing():
    return render_template('info.html', info = 'Pricing Information')

# Settings
@bp.route('/settings/')
def settings():
    return render_template('info.html', info = 'Settings')

# Help
@bp.route('/help/')
def help():
    return render_template('info.html', info = 'Help')

# Cart
@bp.route('/orders/', methods=['POST','GET'])
def order():
    glasses_id = request.values.get('glasses_id')

    # Retrieve order if exists
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
        # Order will be None if order_id stale
    else:
        # There is no order
        order = None

    # Create new order if needed
    if order is None:
        order = Order(status = False, firstname='', surname='', email='', phone='', address_street='', address_city='', address_postcode='', \
            date=datetime.now(), totalcost=0, )
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # Calcultate Total Price
    totalprice = 0
    if order is not None:
        for glasses in order.glasses:
            totalprice = totalprice + glasses.price
            
    # Add Item
    if glasses_id is not None and order is not None:
        glasses = Glasses.query.get(glasses_id)
        if glasses not in order.glasses:
            try:
                order.glasses.append(glasses)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('Item already in basket')
            return redirect(url_for('main.index'))

    itemnumber = len(order.glasses)
    shippingdate = order.date + timedelta(days=3)
    
    return render_template('cart.html', order = order, totalprice = totalprice, itemnumber = itemnumber, shippingdate=shippingdate)

# Delete specific basket items
@bp.route('/deleteorderitem/', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        glasses_to_delete = Glasses.query.get(id)
        try:
            order.glasses.remove(glasses_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))

# Scrap basket
@bp.route('/deleteorder/')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))

# Checkout by Entering Details
@bp.route('/checkout/', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.address_street = form.address_street.data
            order.address_city = form.address_city.data
            order.address_postcode = form.address_postcode.data
            totalcost = 0
            for glasses in order.glasses:
                totalcost = totalcost + glasses.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you for your order!')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('forms.html', form = form, title='finalise your checkout')

# Send the glasses to a friend
@bp.route('/<productname>/friendsend/', methods=['POST','GET'])
def friendsend(productname):
    form = FriendSend() 
    glasses = Glasses.query.filter(Glasses.name == productname)
       
    if form.validate_on_submit():
        flash('We will send this information to the e-mail!')
        return redirect(url_for('main.index', glasses = glasses))

    return render_template('forms.html', form = form, title='send to someone')

# Make an enquiry
@bp.route('/enquiry/', methods=['POST','GET'])
def enquiry():
    form = Help() 

    if form.validate_on_submit():
        flash('Thank you for your enquiry!')
    return render_template('forms.html', form = form, title='make your enquiry')

