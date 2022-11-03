from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError

def validate_content(form, field):
        if len(field.data) < 1:
            raise ValidationError("Tweet must have content!")

class TweetForm(FlaskForm):
    userId = IntegerField("User", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()])
