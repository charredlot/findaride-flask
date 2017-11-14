from os import getenv

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/findroute")
def findroute():
    return render_template("findroute.html")


@app.route("/map")
def mappage():
    return render_template("map.html", api_key=getenv("API_KEY"))
