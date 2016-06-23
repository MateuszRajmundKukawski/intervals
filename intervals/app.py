import os

from flask import Flask, render_template, request
from werkzeug import secure_filename

from intervals.forms import GpxForm
from intervals.tempo import get_data
from intervals.utils import split_list

BASE_DIR = os.path.dirname(os.path.os.path.abspath(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads/')
STATIC_DIR = os.path.join(BASE_DIR, 'static/')
sup = STATIC_DIR

# local
# app = Flask(__name__, static_url_path=sup)
# serwer
app = Flask(__name__, static_folder=STATIC_DIR)
app.secret_key = 's3cr3t'


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload/')
def upload():
    form = GpxForm()
    return render_template('upload.html', form=form)


@app.route('/run/', methods=('GET', 'POST'))
def test_web():
    if request.method == 'POST':
        form = GpxForm()
        if not form.validate_on_submit():
            return 'zjebales, jeszcze raz'
        filename = secure_filename(form.gpx.data.filename)
        upload_path = os.path.join(UPLOADS_DIR, filename)
        form.gpx.data.save(upload_path)
        ccuracy_liczba_probek = int(request.form['ccuracy_liczba_probek'])
        accuracyPaceDiffForIntervalSearch = int(request.form['accuracyPaceDiffForIntervalSearch'])
        point_distance_minimal_between_interwalsS = int(request.form['point_distance_minimal_between_interwalsS'])
        filter_orderS = int(request.form['filter_orderS'])
        wiekS = int(request.form['wiekS'])
        zakresyTetnaProcentyS = split_list(request.form['zakresyTetnaProcentyS'])
        fpath = os.path.join(UPLOADS_DIR, filename)
        base_name, print_list = get_data(
            STATIC_DIR,
            fpath,
            ccuracy_liczba_probek,
            accuracyPaceDiffForIntervalSearch,
            point_distance_minimal_between_interwalsS,
            filter_orderS,
            wiekS,
            zakresyTetnaProcentyS,
        )
        plot_path = os.path.join(STATIC_DIR, base_name)
        if os.path.isfile(plot_path):
            return render_template('plots.html', plot_path=base_name, data_list=print_list, shitt=plot_path)
        else:
            return 'nie ma'

if __name__ == '__main__':
   app.debug = True
   app.run()
