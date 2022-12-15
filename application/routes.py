from datetime import datetime

import pandas as pd
from flask import current_app as app
from flask import jsonify, request
from models import DataRecord

from . import db


@app.route("/api/summary/", methods=["GET"])
def summary():
    datalogger = request.args.get("datalogger")
    if not datalogger:
        return "datalogger id required", 400

    span = request.args.get("span")
    if span:
        if span != "day" and span != "hour" and span != "max":
            return "Available values are day,hour,max", 400

    since, before = request.args.get("since"), request.args.get("before")
    for arg in (since, before):
        if arg:
            try:
                datetime.fromisoformat(arg)
            except:
                return f"Since and Before parameters should be in ISO-8601 format", 400

    # All args have been validated
    query = db.select(DataRecord).where(DataRecord.datalogger == datalogger)
    data = db.session.scalars(query).all()
    df = pd.DataFrame(data)
    df.sort_values(by=["at"], inplace=True)

    # looking for values before
    index = df[df["at"] < before].iloc[-1].name
    values = df.iloc[:index]

    # Looking for values since

    return values.to_json(orient="records")  # Needs reworks to get the right format
