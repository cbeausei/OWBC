import json
import sys

general_stats = [
  ['Rank', 'competitive', 'overall_stats', 'comprank'],
  ['Endorsement level', 'competitive', 'overall_stats', 'endorsement_level'],
  ['Hero damage (1s)', 'competitive', 'rolling_average_stats', 'hero_damage_done'],
  ['Healing (1s)', 'competitive', 'rolling_average_stats', 'healing_done'],
  ['Kill per death ratio', 'competitive', 'game_stats', 'kpd'],
]

heroes = ['brigitte', 'widowmaker', 'reaper', 'reinhardt', 'ana', 'bastion', 'moira', 'dva', 'mei',
'pharah', 'winston', 'symmetra', 'genji', 'zarya', 'zenyatta', 'lucio', 'tracer', 'junkrat',
'torbjorn', 'hanzo', 'roadhog', 'mercy', 'doomfist', 'sombra', 'wrecking_ball', 'orisa',
'soldier76', 'mccree'] 
heroes.sort()

heroes_stats = [
  ['Win percentage', 'stats', 'competitive', 'name', 'general_stats', 'win_percentage'],
  ['Time played (hours)', 'stats', 'competitive', 'name', 'general_stats', 'time_played'],
  ['Weapon accuracy', 'stats', 'competitive', 'name', 'general_stats', 'weapon_accuracy'],
  ['Hero damage (1s)', 'stats', 'competitive', 'name', 'rolling_average_stats', 'hero_damage_done'],
  ['Healing (1s)', 'stats', 'competitive', 'name', 'rolling_average_stats', 'healing_done'],
  ['Barrier damage (1s)', 'stats', 'competitive', 'name', 'rolling_average_stats',
  'barrier_damage_done'],
  ['Eliminations', 'stats', 'competitive', 'name', 'rolling_average_stats', 'eliminations'],
]

friends = ['bc', 'popof', 'saroupille']

def read_json(json_file):
  with open (json_file, 'r') as f:
    data = json.load(f)
  return data

def parse_data(data):
  if 'us' in data:
    return data['us']
  if 'eu' in data:
    return data['eu']
  if 'kr' in data:
    return data['kr']

friends_data = {}
friends_hero = {}
for friend in friends:
  data = parse_data(read_json(friend + '.json'))
  friends_data[friend] = data
  hero_played = []
  for hero in heroes:
    if hero in data['heroes']['stats']['competitive']:
      hero_played.append((-data['heroes']['stats']['competitive'][hero]['general_stats']['time_played'], hero))
  hero_played.sort()
  friends_hero[friend] = hero_played
  sys.stderr.write('Player ' + friend + ' stats loaded.\n')
players_data = [parse_data(data) for tag, data in read_json('save_stats.json').iteritems()]
sys.stderr.write('Players stats loaded.\n')

general_json = []
for stat in general_stats:
  line = [stat[0]]
  for friend in friends:
    s = friends_data[friend]['stats']
    for x in stat[1:]:
      s = s[x]
    try:
      line.append('%.2f' % s)
    except:
      line.append('N/A')
  nb = 0.0
  mean = 0.0
  for data in players_data:
    try:
      s = data['stats']
      for x in stat[1:]:
        s = s[x]
      mean += s
      nb += 1
    except:
      pass
  if nb > 0:
    line.append('%.2f' % (mean / nb))
  else:
    line.append('N/A')
  general_json.append(line)
for i in range(3):
  line = ['Hero #' + str(i + 1)]
  for friend in friends:
    line.append(friends_hero[friend][i][1].capitalize());
  general_json.append(line)
sys.stderr.write('General stats computed.\n')

table_json = []
table_json.append({'key': 'General', 'value': general_json})

for hero in heroes:
  hero_json = []
  for stat in heroes_stats:
    line = [stat[0]]
    for friend in friends:
      try:
        s = friends_data[friend]['heroes']
        for x in stat[1:]:
          if x == 'name':
            s = s[hero]
          else:
            s = s[x]
        line.append('%.2f' % s)
      except:
        line.append('N/A')
    nb = 0.0
    mean = 0.0
    for data in players_data:
      try:
        s = data['heroes']
        for x in stat[1:]:
          if x == 'name':
            s = s[hero]
          else:
            s = s[x]
        mean += s
        nb += 1
      except:
        pass
    if nb != 0:
      line.append('%.2f' % (mean / nb))
    else:
      line.append('N/A')
    hero_json.append(line)
    #sys.stderr.write('Stat "' + stat[0] + '" computed.\n')
  sys.stderr.write(hero.capitalize() + ' stats computed.\n')
  table_json.append({'key': hero.capitalize(), 'value': hero_json})

with open('table.json', 'w') as f:
  json.dump(table_json, f)
