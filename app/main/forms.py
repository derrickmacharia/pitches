from wtforms import StringField,TextAreaField, SubmitField, SelectField
from wtforms.validators import Required
from flask_wtf import FlaskForm


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post_title = StringField('Post title', validators=[Required()])
    post_category = SelectField('Post category',choices=[('Select a category','Select a category'),('Pickup lines', 'Pickup lines'),('Interview','Interview'),('Product','Product'),('Promotions','Promotions')], validators=[Required()])
    comment = StringField('What is in your mind?')
    submit = SubmitField('Submit')