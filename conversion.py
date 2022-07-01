from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def firstTemplate():
    return render_template('base.html')

@app.route("/about")
def aboutTemplate():
    return render_template('about.html')