import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################



@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/<start>/<end>"
        
        
    )   


@app.route("/api/v1.0/precipitation")
def precipitation():
    '''somethiong'''
   # Calculate the date 1 year ago from the last data point in the database
    lastdate = session.query(Measurement.date).order_by(Measurement.date.desc()).all()
    lastdate = lastdate[0]
    lastdate = str(lastdate)
    lastdate = lastdate.replace(',', '')
    lastdate = lastdate.replace('(', '')
    lastdate = lastdate.replace(')', '')
    lastdate = lastdate.replace("'", '')
    lastdate = lastdate.replace("", '')
    lastdate = dt.datetime.strptime(lastdate, '%Y-%m-%d')
    lastyear =  lastdate - dt.timedelta(days=365)
    # Perform a query to retrieve the data and precipitation scores
    query = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= lastyear).\
    order_by(Measurement.date.asc()).all()
    return jsonify({k:v for k,v in query})
    


@app.route("/api/v1.0/stations")
def stations():
    query_active_station = session.query(Measurement.station, func.count(Measurement.id))\
                       .group_by(Measurement.station)\
                       .order_by(func.count(Measurement.id).desc()).all()
    return jsonify({i:j for i,j in query_active_station.desc()})

@app.route("/api/v1.0/<start>")

    


@app.route("/api/v1.0/<start>/<end>")
def names(start = None, end = None):
	
	if not end:
		end = datetime.now()
    
    
if __name__ == '__main__':
    app.run(debug=True)
