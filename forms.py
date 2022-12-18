from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange, AnyOf, Email

class LuckyNumForm(FlaskForm):
    """ Form for validating input to the API endpoint. """
    # I could not get @csrf.exempt or app.config[WTF_CSRF_CHECK_DEFAULT] = FALSE
    # to work, I was about to give up on the extra credit and then I found this,
    # which ended up working. Granted, I don't really understand it, but I'll
    # take it for now. I assume it just sets the token requiremnt to false for
    # this particular form validation.
    class Meta:
        csrf = False

    name = StringField('Name', validators=[InputRequired("Input required.")])
    email = StringField('Email', validators=[InputRequired("Input required."), Email()])
    year = IntegerField('Year',
        validators=[
            InputRequired("Input required."),
            NumberRange(1900, 2000, "Year range must be between 1900 and 2000")
        ])
    color = StringField('Color',
                    validators=[InputRequired("Input required."),
                    AnyOf(values=["blue", "green", "red", "orange"])])