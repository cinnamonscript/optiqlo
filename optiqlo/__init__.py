# Import flask - from the package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app=Flask(__name__)

# Create a function that creates a web application
# A web server will run this web application
def create_app():
    app.debug=True
    app.secret_key='Hehehe123'

    # Set the app configuration data
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///optiqlo'

    # Initialise db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)
    
    # Importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)
    
    # This is used to import my Database.
    from . import admin
    app.register_blueprint(admin.bp)
   
    return app

# Inbuilt function which takes error as parameter 
@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html")

@app.errorhandler(500)
def internal_error(e):
  return render_template("500.html")

