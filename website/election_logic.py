def parse_winning_party(data):
  predictions = []
  for row in data:
    added = 0
    party = row[0]
    state = row[1]
    price = row[3]

    #check if state in predictions already
    for pred in predictions:
      if pred['state'] == state:
        if pred['price'] < price:
          pred['party'] = party
          pred['price'] = price
        added = 1
    
    if added == 0:
      predictions.append({'state': state,
        'party': party,'price': price})

  return predictions

#need to pass the resutls of parse_winning_party to this as data
def weighted_prediction(data):
  #read in the electoral votes of each state
  with open('state_electoral_vote_count.csv','r') as f:
    elect_votes = {}
    for line in f:
      x = line.split(',')
      elect_votes[x[0]] = int(x[1])

  rep_votes = 0
  dem_votes = 0
  
  for datum in data:
    if(datum['party'] == 'Republican'):
      rep_votes+= elect_votes[datum['state']]
    else:
      dem_votes+= elect_votes[datum['state']]

  return{'rep': rep_votes, 'dem': dem_votes}

