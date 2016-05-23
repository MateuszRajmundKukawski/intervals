from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired

class GpxForm(Form):
    gpx = FileField('Your gpx file', validators=[
        FileRequired(),
        FileAllowed(['gpx', 'txt'], 'Gpx only!')
    ])
