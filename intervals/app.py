import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
from intervals.tempo import get_data

from intervals.forms import GpxForm, ParamsForm

BASE_DIR = os.path.dirname(os.path.os.path.abspath(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads/')
STATIC_DIR = os.path.join(BASE_DIR, 'static/')
sup = STATIC_DIR
print STATIC_DIR

# static_url_path="static", static_folder="static"

# app = Flask(__name__, static_folder=STATIC_DIR, static_url_path=STATIC_DIR)
# local
app = Flask(__name__, static_url_path=sup)
# serwer
# app = Flask(__name__, static_folder=STATIC_DIR)
app.secret_key = 's3cr3t'


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload/', methods=('GET', 'POST'))
def upload():
    form = GpxForm()
    form_params = ParamsForm()
    if form.validate_on_submit():
        filename = secure_filename(form.gpx.data.filename)
        upload_path = os.path.join(UPLOADS_DIR, filename)
        form.gpx.data.save(upload_path)
    else:
        filename = None
    return render_template('upload.html', form=form)

@app.route('/run/', methods=('GET', 'POST'))
def make_plots():
    if request.method == 'POST':
        fname = request.form['gpx']
        # accuracyPaceDiffForIntervalSearch = request.form['accuracyPaceDiffForIntervalSearch']
        # print accuracyPaceDiffForIntervalSearch
        ccuracy_liczba_probek = int(request.form['ccuracy_liczba_probek'])
        accuracyPaceDiffForIntervalSearch = int(request.form['accuracyPaceDiffForIntervalSearch'])
        point_distance_minimal_between_interwalsS = int(request.form['point_distance_minimal_between_interwalsS'])
        filter_orderS = int(request.form['filter_orderS'])
        wiekS = int(request.form['wiekS'])
        zakresyTetnaProcentyS = int(request.form['zakresyTetnaProcentyS'])

        print accuracyPaceDiffForIntervalSearch, type(accuracyPaceDiffForIntervalSearch)
        print point_distance_minimal_between_interwalsS
        print filter_orderS
        print wiekS
        print zakresyTetnaProcentyS
        zakresyTetnaProcentyS = [54, 63, 73, 81, 91, 100]



        fpath = os.path.join(UPLOADS_DIR, fname)
        print 'fpath', fpath
        raw_input('??????????????????????????????')
        base_name, print_list = get_data(
            STATIC_DIR,
            fpath,
            ccuracy_liczba_probek,
            accuracyPaceDiffForIntervalSearch,
            point_distance_minimal_between_interwalsS,
            filter_orderS,
            wiekS,
            zakresyTetnaProcentyS,
            #
            # output_dir,
            # fileName,
            # ccuracy_liczba_probek,
            # accuracy_pace_diff_for_interval_search,
            # point_distance_minimal_between_interwals,
            # filter_order,
            # wiek,
            # zakresyTetnaProcenty


        )
        plot_path = os.path.join(STATIC_DIR, base_name[:-3] + 'png')
        print 'plot_path', plot_path
        if os.path.isfile(plot_path):
            return render_template('plots.html', plot_path=base_name, data_list=print_list)
        else:
            return 'nie ma'
    else:
        return render_template('plots.html')


@app.route('/test/', methods=('GET', 'POST'))
def test_web():
    if request.method == 'POST':
        form = GpxForm()
        filename = secure_filename(form.gpx.data.filename)
        upload_path = os.path.join(UPLOADS_DIR, filename)
        form.gpx.data.save(upload_path)
        ccuracy_liczba_probek = int(request.form['ccuracy_liczba_probek'])
        accuracyPaceDiffForIntervalSearch = int(request.form['accuracyPaceDiffForIntervalSearch'])
        point_distance_minimal_between_interwalsS = int(request.form['point_distance_minimal_between_interwalsS'])
        filter_orderS = int(request.form['filter_orderS'])
        wiekS = int(request.form['wiekS'])
        zakresyTetnaProcentyS = [int(x) for x in request.form['zakresyTetnaProcentyS'].split()]

        # filename = secure_filename(form.gpx.data.filename)
        # upload_path = os.path.join(UPLOADS_DIR, filename)[:-3]+'png'
        # plot_path = os.path.join(STATIC_DIR, base_name[:-3] + 'png')
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
            #
            # output_dir,
            # fileName,
            # ccuracy_liczba_probek,
            # accuracy_pace_diff_for_interval_search,
            # point_distance_minimal_between_interwals,
            # filter_order,
            # wiek,
            # zakresyTetnaProcenty

        )
        plot_path = os.path.join(STATIC_DIR, base_name)
        if os.path.isfile(plot_path):
            return render_template('plots.html', plot_path=base_name, data_list=print_list, shitt=plot_path)
        else:
            return 'nie ma'
    # return render_template('plots.html')

if __name__ == '__main__':
   app.debug = True
   app.run()
