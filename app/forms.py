from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ProjectForm(FlaskForm):
    projectDescriptionOneLine = TextAreaField('Description', validators=[DataRequired()])
    projectDescription = TextAreaField('Description', validators=[DataRequired()])
    
    
    projectWishes = SelectField('ProjectWishes', choices = [('company', 'A company'), 
      ('NGO', 'A non-profit'), ('research', 'Important research'), 
      ('art', 'Iconic art work'), """JULIUS Add other option"""])
    
    projectPlans = StringField('Description', validators=[DataRequired()])
    mainCategory = StringField('Category', validators=[DataRequired()])
    otherCategory1 = StringField('Category', validators=[DataRequired()])
    otherCategory2 = StringField('Catgeory', validators=[DataRequired()])

    submit = SubmitField('Save')