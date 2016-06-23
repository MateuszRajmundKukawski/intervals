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
        default=10)
    point_distance_minimal_between_interwalsS = IntegerField(
        'accuracyPaceDiffForIntervalSearch',
        [
            validators.DataRequired(),

        ],
        default=1)
    filter_orderS = IntegerField(
        'ccuracy_liczba_probek',
        [
            validators.DataRequired(),

        ],
        default=5)
    wiekS = IntegerField(
        'ccuracy_liczba_probek',
        [
            validators.DataRequired(),

        ],
        default=30)
    zakresyTetnaProcentyS = StringField(
        'ccuracy_liczba_probek',
        [
            validators.DataRequired(),

        ],
        default="8 54 63 73 81 91 100")

# CCURACY_LICZBA_PROBEK = 8  # ile kolejnych probek ma byc wieksze (dla szukania startu) badz mniejsze (dla stopu) od probki aktualnie iterowanej
# accuracyPaceDiffForIntervalSearch = 1  # jakiej roznicy tempa (min / km) ma szukac
# point_distance_minimal_between_interwalsS = 10  # dla ilu kolejnych punktow olewac start / stop interwalu (jezeli jest 'dlugi rozped')
# filter_orderS = 5  # liczba probek do usrednienia, dla latwiejszego wykrywania startu / stopu
# # usredniam dane z x probek, przebieg robi sie mniej poszarpany, na wykresie sa wartosci oryginalne
# wiekS = 30
# zakresyTetnaProcentyS = [54, 63, 73, 81, 91, 100]
class ParamsForm(Form):
    ccuracy_liczba_probek = IntegerField(
        'ccuracy_liczba_probek',
        [
            validators.DataRequired(),

         ])
    accuracyPaceDiffForIntervalSearch = IntegerField(
        'accuracyPaceDiffForIntervalSearch',
        [
            validators.DataRequired(),

        ])
    point_distance_minimal_between_interwalsS = IntegerField(
        'accuracyPaceDiffForIntervalSearch',
        [
            validators.DataRequired(),

        ])
    filter_orderS = IntegerField(
        'ccuracy_liczba_probek',
        [
            validators.DataRequired(),

        ])
    wiekS = IntegerField(
        'ccuracy_liczba_probek',
        [
            validators.DataRequired(),

        ])
    zakresyTetnaProcentyS = IntegerField(
        'ccuracy_liczba_probek',
        [
            validators.DataRequired(),

        ])
