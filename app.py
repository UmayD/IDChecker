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
        turkish_id = request.form['content'] # Take input from user
        output = IDChecker.takeID(turkish_id) # Check and return the result of validation
        return render_template("checked.html", output=output) # Pass the validated result to the html
    else:
        return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)