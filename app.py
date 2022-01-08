from flask import Flask, render_template, request
import pandas as pd
import numpy as np


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("pw_page.html")


@app.route("/generate_pw", methods = ['POST'])
def create_pw():
    print(request.form)

    return "Working"