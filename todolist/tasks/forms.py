from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, NumberRange
import datetime

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    priority = IntegerField("Priority", default=4, validators=[NumberRange(1, 4)])
    scheduled_date = DateTimeField("Schedule Task", format="%Y-%m-%d", default=datetime.datetime.now)
    submit = SubmitField('Submit')
