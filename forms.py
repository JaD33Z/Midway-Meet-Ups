from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LocationForm(FlaskForm):
    start_point = StringField("Your Location", validators=[DataRequired()])
    end_point = StringField("Their Location", validators=[DataRequired()])
    submit = SubmitField('Submit')


class MidwayForm(FlaskForm):
    town_name = StringField("Name Of Town Midway", validators=[DataRequired()])
    state_name = StringField("Name Of State", validators=[DataRequired()])
    place_category = StringField("Type of Place - Use single keywords as: restaurants, pub, cafe, park, library, etc.", validators=[DataRequired()])
    submit = SubmitField("Submit")