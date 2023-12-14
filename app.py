# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

#################################################
# Database Setup
engine = create_engine("sqlite:///../Resources/mammal_masses.sqlite", echo=False)
 
# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(autoload_with=engine)

# Save references to each table
measurements = base.classes.weather
station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def Welcome():
    return(
    """List all available api routes."""
       return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"

    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""
    # Calculate the date 1 year ago from last date in database
    prev_year = date.date(2017, 8, 23) - date.timedelta(days=365)
    
        # Query for the date and precipitation for the last year
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

    
    # Dict with date as the key and prcp as the value
    #jsonify to clean up formatting, {} to take the values last year
        Dictionary_1 = {date: prcp}
        return = jsonify(prcp)
        
        
@app.route("/api/v1.0/stations")

    # Unravel results into a 1D array and convert to a list
# define a stations function to return query
def stations()
'''return list of stations'''
results = session.query(station).all

#reset session to refresh objects
session.close()
#  used to change a 2-d array to 1d
stations = array(np.ravel(results))
# print out array
    return jsonify(stations) 


@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temperature observations (tobs) for previous year."""
    # Calculate the date 1 year ago from last date in database
        prev_year = date.date(2017, 8, 23) - date.timedelta(days=365)

        # Query the primary station for all tobs from the last year
    # Unravel results into a 1D array and convert to a list
    # Return the results
    results = session.query(Measurement.tobs).filter(Measurement.date >= prev_year).all()
#reset session to refresh objects
session.close()
#  used to change a 2-d array to 1d
tobs = array(np.ravel(results))
# print out array
    return jsonify(tobs) 

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""

    # Summarize in stats and return min, max, avg temps
    
    summary_data = [[measurement.date], [measurement.tobs.descibe()]
    return jsonify(summary_temps)

        
            # calculate TMIN, TAVG, TMAX with start and stop
    # Unravel results into a 1D array and convert to a list
summary_data = list(np.ravel(results))
return jsonify(tobs)

# User input and call app
if __name__ == '__main__':
    app.run()