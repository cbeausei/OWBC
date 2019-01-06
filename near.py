import requests
import sys
import json
import time

url = 'https://owapi.net/api/v3/u/'
headers = {
    'User-Agent': 'Mozilla/5.0',
}

def get_data(tag):
    return json.loads(requests.get(url + tag + '/blob', headers = headers).content)

def get_rank(data):
    if 'us' in data:
        return data['us']['stats']['competitive']['overall_stats']['comprank']
    if 'eu' in data:
        return data['eu']['stats']['competitive']['overall_stats']['comprank']
    if 'kr' in data:
        return data['kr']['stats']['competitive']['overall_stats']['comprank']

def read_tags():
    tags = {}
    with open('tags.txt') as f:
        for line in f.readlines():
            tag, rank = line.split()
            rank = int(rank)
            if rank not in tags:
                tags[rank] = []
            tags[rank].append(tag)
    return tags

data_stats = {}
tags = read_tags()
for r in range(1880, 2050, 2):
  sys.stderr.write(str(r) + '\n')
  for tag in tags[r]:
    tag = tag.replace('#', '-')
    sys.stderr.write(tag + '\n')
    try:
      data_stats[tag] = get_data(tag)
    except:
      pass
    time.sleep(6)
print(len(data_stats))
with open('stats.json', 'w') as f:
    json.dump(data_stats, f)
