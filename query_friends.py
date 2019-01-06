import requests
import json
import time
import sys

url = 'https://owapi.net/api/v3/u/'
headers = {
    'User-Agent': 'Mozilla/5.0',
}
friends = [('saroupille', 'Saroupille-2528'), ('popof', 'popof-2696'), ('bc', 'Choundeh-2324')]

def get_data(tag):
  return json.loads(requests.get(url + tag + '/blob', headers = headers).content)

for friend, tag in friends:
  wait = 1
  sys.stderr.write(friend)
  while True:
    time.sleep(wait)
    sys.stderr.write('.')
    wait += 1
    data = get_data(tag)
    if 'error' not in data:
      break
  sys.stderr.write('done\n')
  with open(friend + '.json', 'w') as f:
    json.dump(data, f)
