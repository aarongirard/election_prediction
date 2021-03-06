import requests, time, multiprocessing, os, sys, threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import add_record_StateElectoralCollege_table

def log(error):
  with open('log_exceptions.txt', 'a+') as f:
    f.write(str(str(int(time.time())) + ' :' + error+'\n'))

#returns json of requested states' data
def get_request_by_state(state):
  url = 'https://www.predictit.org/api/marketdata/ticker/'+state+'.USPREZ16'
  try:
    r= requests.get(url,headers={'Accept': 'applicatoin/json'})
  except requests.exceptions.RequestException as e:
    log(str(e))
    return 0
  return r.json()

#returns list of dictionaries;formated specified for add to DB
#one for each party
def parse_json(json):
  contracts = []
  for contract in json['Contracts']:
    pred = {}
    pred['name'] = contract['Name']
    pred['lastcloseprice'] = contract['LastTradePrice']
    pred['time'] = int(time.time()) #utc timestamp
    contracts.append(pred)
  return contracts

def run_one_state(state):
  #print ' requesting ', state
  req_json = get_request_by_state(state)
  if req_json != 0:
    values = parse_json(req_json)
    for val in values:
      val['state'] = state #add state value
      add_record_StateElectoralCollege_table(val)


def main():
  #run every 60 minutes
  while True:
    with open('states.txt','r') as f:
      threads = []
      for line in f:
        line = line.strip()
        t = threading.Thread(target=run_one_state, args=(line,))
        threads.append(t)
        try:
          #print 'starting thread'
          t.start()
        except e:
          log(str(e))
        #p = multiprocessing.Process(target=run_one_state, args=(line,))
        #p.start()
        #run_one_state(line)
    time.sleep(60)#60*60

  
if __name__ == '__main__':
    main()
