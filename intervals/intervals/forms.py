from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextField, IntegerField, validators,StringField


class GpxForm(Form):
    gpx = FileField('Your gpx file', validators=[
        FileRequired(),
        FileAllowed(['gpx', 'txt'], 'Gpx only!')
    ])

    ccuracy_liczba_probek = IntegerField(
        'ccuracy_liczba_probek',

        [
            validators.DataRequired()

        ],
        default=8) # 8 10 1 5 3
    accuracyPaceDiffForIntervalSearch = IntegerField(
        'accuracyPaceDiffForIntervalSearch',
        [
            validators.DataRequired(),

        ],
        default=1)
    point_distance_minimal_between_interwalsS = IntegerField(
        'point_distance_minimal_between_interwalsS',
        [
            validators.DataRequired(),

        ],
        default=10)
    filter_orderS = IntegerField(
        'filter_orderS',
        [
            validators.DataRequired(),

        ],
        default=5)
    wiekS = IntegerField(
        'wiekS',
        [
            validators.DataRequired(),

        ],
        default=30)
    zakresyTetnaProcentyS = StringField(
        'zakresyTetnaProcentyS',
        [
            validators.DataRequired(),

        ],
        default="54 63 73 81 91 100")
