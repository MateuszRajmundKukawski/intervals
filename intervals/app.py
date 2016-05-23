import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
from intervals.tempo import get_data

from intervals.forms import GpxForm

BASE_DIR = os.path.dirname(os.path.os.path.abspath(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads/')
STATIC_DIR = os.path.join(BASE_DIR, 'static/')
sup = STATIC_DIR
print STATIC_DIR
#app = Flask(__name__, static_url_path=sup)

# static_url_path="static", static_folder="static"
app = Flask(__name__, static_folder=STATIC_DIR, static_url_path=STATIC_DIR)
# app = Flask(__name__, static_folder=STATIC_DIR)
app.secret_key = 's3cr3t'


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload/', methods=('GET', 'POST'))
def upload():
    form = GpxForm()
    if form.validate_on_submit():
        filename = secure_filename(form.gpx.data.filename)
        upload_path = os.path.join(UPLOADS_DIR, filename)
        form.gpx.data.save(upload_path)
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)

@app.route('/run/', methods=('GET', 'POST'))
def make_plots():
    if request.method == 'POST':
        fname = request.form['fname']
        fpath = os.path.join(UPLOADS_DIR, fname)
        print 'fpath', fpath
        base_name, print_list = get_data(STATIC_DIR, fpath)
        plot_path = os.path.join(STATIC_DIR, base_name[:-3] + 'png')
        print 'plot_path', plot_path
        if os.path.isfile(plot_path):
            return render_template('plots.html', plot_path=base_name, data_list=print_list)
        else:
            return 'nie ma'
    else:
        return render_template('plots.html')

if __name__ == '__main__':
   app.debug = True
   app.run()
