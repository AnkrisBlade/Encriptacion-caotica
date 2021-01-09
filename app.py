from flask import Flask, url_for,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", name="Index")

#URL CSS
#url_for('static', filename='style.css')