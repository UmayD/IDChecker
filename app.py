from flask import Flask, render_template, request
from datetime import datetime

from checker import IDChecker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        turkish_id = request.form['content']
        output = IDChecker.takeID(turkish_id)
        return render_template("idchecker.html", output=output)
    else:
        return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)