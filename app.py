# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# #make sure to run the export and set in the terminal 
# #export FLASK_APP=app.py
# #set FLASK_APP=app.py
# #def home():
#     #return "Hello, Flask!"

# def practice_skills():
#     return "Hello starshine, the world says HELLOOOOOooo :) -- Johnny Depp"
#when running the flask- if the return changes save it quit the previous run and
#rerun it for the new message to appear 

import datetime as dt
import numpy as np
import pandas as pd

#dependencies needs for SQLAlchemy 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# 
from flask import Flask, jsonify

#start the set up and access of the SQLite database 
engine = create_engine("sqlite:///hawaii.sqlite")

#then we add the function to access the query within SQLite
Base = automap_base()
#next we use ______ to reflect the tables into Alchemy 

Base.prepare(engine, reflect= True)
#set the variables
Measurement = Base.classes.measurement
Station = Base.classes.station

#make the session link
session = Session(engine)

app = Flask(__name__)
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
#when running make sure to run the http: then attach the "/api/....."
#so it follows directly to that specifies action

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
#should run null null null- if you run the app.route
#/api/v1.0/temp/2017-06-01/2017-06-30 give you specified dates,thus youll get specified data outputs 

