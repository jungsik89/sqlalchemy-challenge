import datetime as dt
# import numpy as np
# import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite://Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)
#[what i want to return           looping           if statement]
#{   k:v                      for k,v in tuple


app = Flask(__name__)
    
@app.route("/")
def index():
    """List all available api routes."""

    homepage = """
        /api/v1.0/precipitation<br>
        /api/v1.0/stations<br>
        /api/v1.0/tobs<br>
        /api/v1.0/start_date<br>
        /api/v1.0/start_date/end_date<br>
        """
    return homepage
    
if __name__ == "__main__":
    #run the code
    app.run()
    




# @app.route("/api/v1.0/precipitation")
# def precipitation():
    # '''something'''
    # '''put your precipitation query here'''
    # query = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= "2016-08-23").order_by(Measurement.date.asc()).all()
    
    # return jsonify({k:v for k,v in query})
    
    
    
        
# @app.route("/api/v1.0/stations")
# def stations():
    # '''do something'''


# @app.route("/")
# def welcome():
    # return(
        # f"Available Router:<br/>"
        # f"/api/v1.0/precipitation:<br/>"
        # f"/api/v1.0/stations:<br/>"
        
        
# @app.route("/<start></end>")
# @app.route("/<start>")
# def names(start = None, end = None):
    # if not end:
    # end = datetime.now()

        
        
        

