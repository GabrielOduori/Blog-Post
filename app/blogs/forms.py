# blog_posts/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    body = TextAreaField('Text',validators=[DataRequired()])
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):
    body = TextAreaField('Text',validators=[DataRequired()])
    submit = SubmitField("Submit")




