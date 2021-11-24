from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img = request.files['image']

        filename = secure_filename(img.filename)

        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        img.save(path)

        return redirect(url_for("result", result=path))

    # Homepagina
    return render_template('index.html')


@app.route('/result', methods=['GET'])
def result():
    result = request.args['result']
    return send_file(result, mimetype='image/gif')


app.run(port=5000, debug=True)
