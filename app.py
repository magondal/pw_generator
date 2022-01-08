from flask import Flask, render_template
import pandas as pd
import numpy as np
app = Flask(__name__)
@app.route("/")
def homepage():
    return "Evan", 200