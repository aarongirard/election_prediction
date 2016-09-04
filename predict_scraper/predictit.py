import requests
import time
import multiprocessing

from database import add_record_StateElectoralCollege_table

def log(error):
  with open('log_exceptions.txt', 'a+') as f:
    f.write(error+'\n')

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

def run_one_state(state,i):
  #print ' requesting ', state
  req_json = get_request_by_state(state)
  if req_json != 0:
    values = parse_json(req_json)
    for val in values:
      val['state'] = line #add state value
      add_record_StateElectoralCollege_table(val)
  print i


def main():
  #run every 5 minutes
  while True:
    with open('states.txt','r') as f:
      i=0
      for line in f:
        line = line.strip()
        p = multiprocessing.Process(target=run_one_state, args=(line,i))
        p.start()
        i+=1
        #run_one_state(line)
    time.sleep(300)#60*5

  
if __name__ == '__main__':
    main()