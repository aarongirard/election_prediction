import os, sys
from flask import Flask, request, session, g, redirect, url_for, abort, \
  render_template, flash

#hacks to import file in parent dir
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import database

def log(thing_to_log):
  with open('log.txt', 'a+') as f:
    f.write(str(thing_to_log) + '\n')

#create the application
app = Flask(__name__)


#testings
@app.route('/state_predictit_prediction', methods=['get','post'])
def hello_world():
    


if __name__ == '__main__':
  app.run(host='localhost', port = 8000)