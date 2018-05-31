from flask import Flask, render_template, request, jsonify, current_app, send_from_directory
from werkzeug.utils import secure_filename
import datetime
import os
from speaker.demo.demo_diarization import *


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/diarize', methods=['POST', 'GET'])
def diarize_api():
    #return jsonify(request.files)
    if 'audio' not in request.files:
        return jsonify({'message': 'No file upload.'})
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'message': 'No selected file.'})
    elif file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'] + "/" + datetime.date.today().strftime("%B-%d-%Y-%H-%M-%S%p"))):
            os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'] + "/" + datetime.date.today().strftime("%B-%d-%Y-%H-%M-%S%p")), 777)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/" + datetime.date.today().strftime("%B-%d-%Y-%H-%M-%S%p") + "/", filename))
        #print({'result': todiarize(os.path.join(app.config['UPLOAD_FOLDER'] + "/" + datetime.date.today().strftime("%B-%d-%Y-%H-%M-%S%p") + "/", filename))})
        return jsonify({'result': todiarize(os.path.join(app.config['UPLOAD_FOLDER'] + "/" + datetime.date.today().strftime("%B-%d-%Y-%H-%M-%S%p") + "/", filename))})
    else:
        return jsonify({'message': 'An error occured'})

"""
@app.route('/diarizedemo')
def diarize_demo():
    print({'result': todiarize(os.path.join(app.config['UPLOAD_FOLDER'] + "/" ,"2.wav"))})
    return jsonify({'message': 'An error occured'}) 
"""

@app.route('/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    dir = current_app.root_path
    return send_from_directory(directory=dir, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
