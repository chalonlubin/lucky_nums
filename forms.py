from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField
from wtforms.validators import InputRequired, NumberRange, AnyOf

class ValidationForm(FlaskForm):
    """ Form for validating input to the API endpoint. """
    class Meta:
        csrf = False

    name = StringField('Name', validators=[InputRequired("Input required.")])
    email = EmailField('Email', validators=[InputRequired("Input required.")])
    year = IntegerField('Year',
        validators=[
            InputRequired("Input required."),
            NumberRange(1900, 2000, "Year range must be between 1900 and 2000")
        ])
    color = StringField('Color',
                    validators=[InputRequired("Input required."),
                    AnyOf(values=["blue", "green", "red", "orange"])])