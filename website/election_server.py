import os, sys
from flask import Flask, request, session, g, redirect, url_for, abort, \
  render_template, flash
import json
import election_logic

#hacks to import file in parent dir
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import database
import creds

HOST = creds.credentials['host']
PORT = creds.credentials['port']

def log(thing_to_log):
  with open('log.txt', 'a+') as f:
    f.write(str(thing_to_log) + '\n')

#create the application
app = Flask(__name__)


#testings
"""
example returned data from database call: 
Democratic|MN|1473050350|0.86
Republican|MN|1473050350|0.15
Democratic|MO|1473050350|0.22
Republican|MO|1473050350|0.78
(its in tuples)

--> convert it to json

"""
@app.route('/electoral_vote_prediction',methods=['get'])
def weighted_EV_prediction():
  data = database.get_most_recent_record_foreach_state('../')
  predictions = election_logic.parse_winning_party(data)
  w_predictions = election_logic.weighted_prediction(predictions)

  return json.dumps(w_predictions)


@app.route('/us_geojson', methods=['get'])
def get_election_map_geojson():
  #read data as json, then return it
  #need to optimize using topojson
  #us.json for geojson
  with open('us.json', 'r') as f:
    data = json.load(f)

  return json.dumps(data)

@app.route('/map', methods=['get'])
def election_map():
  return render_template('map.html')

@app.route('/state_predictit_prediction', methods=['get'])
def predictit_prediction_data_api():
    data = database.get_most_recent_record_foreach_state('../')
    
    #parse out the party who is winning
    predictions = election_logic.parse_winning_party(data)
    
    #return as json    
    data_as_json = json.dumps(predictions)
    return data_as_json

if __name__ == '__main__':
  app.run(host=HOST, port = PORT)
