#coding:utf-8

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/grids')
def grids():
    return render_template("grids.html")

@app.route('/styles')
def styles():
    return render_template('styles.html')
if __name__ == "__main__":
    app.run()
