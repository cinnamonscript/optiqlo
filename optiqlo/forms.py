from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in basket
class CheckoutForm(FlaskForm):
    firstname = StringField("Your first name", validators=[InputRequired()])
    surname = StringField("Your surname", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    phone = StringField("Your phone number", validators=[InputRequired()])
    address_street = StringField("Your street address", validators=[InputRequired()])
    address_city = StringField("Your city", validators=[InputRequired()])
    address_postcode = StringField("Your postcode", validators=[InputRequired()])
    submit = SubmitField("Submit")

class FriendSend(FlaskForm):
    email = StringField("Your email", validators=[InputRequired(), email()])
    submit = SubmitField("Submit")

class Help(FlaskForm):
    name = StringField("Your name", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    enquiry = StringField("Your enquiry", validators=[InputRequired()])
    submit = SubmitField("Submit")
