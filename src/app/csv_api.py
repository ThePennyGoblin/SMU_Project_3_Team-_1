#ETL pt1 raw csv into DB (rearchitect to this)
#API GEN png directly from DB
#Webserver communicates with client and API< JS fits in here

#call imports outside of function. 

#API and webserver usually split in real life 

#standard library, non-standard

from flask import Flask, send_file, render_template    #, jsonify
from data_transform import weight_histogram

# CONSTANTS?
PLOT_PATH = "tmp"

app = Flask(__name__)


########################################
# API Routes
########################################
@app.route("/api/v1.0/tstats/<start_date>")
def tstats(start_date):
    # session = Session(engine)
    path= weight_histogram(start_date, PLOT_PATH)
    # session.close()
    return send_file(path)


########################################
# HTML Routes (front-end)
########################################
#return render template -- replicate bellybutton 
#API call JS can call the API in drop down 


#############################
# prevents from running unless this is named app.py
if __name__ == '__main__':
    app.run(debug=True)