from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
import predict


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img = request.files['image']

        filename = secure_filename(img.filename)

        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        img.save(path)

        prediction = predict.predict(path)

        return render_template('result.html', prediction=prediction)

    # Homepagina
    return render_template('index.html')


app.run(port=4000, debug=True)
