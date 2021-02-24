from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.validators import DataRequired 





class UploadForm(FlaskForm):
	"""docstring for UploadForm"""
	upload =  FileField('Image', validators=[FileRequired(),FileAllowed(['jpg','png']'JPG and PNG images are required')])
	submit = SubmitField(Submit)