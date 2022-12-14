from flask import current_app as app
from flask import jsonify, render_template, request, send_file, redirect, url_for
import pandas as pd
from io import BytesIO


@app.route("/", methods=["GET"])
def index():
    return render_template("layout.jinja2")
