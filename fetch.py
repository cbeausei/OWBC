import requests
import sys

url = 'https://overwatchtracker.com/leaderboards/pc/global/CompetitiveRank?page='

def open_page(n):
    return requests.get(url + str(n), cookies={'__test': '2876476287978924867249837'})

def get_tags(page):
    for player in page.split('<tr class="">')[1:]:
        tag = player.split('">')[2].split('</a>')[0]
        rank = int(player.split('bold;">')[1].split('</span>')[0])
        print tag, rank

for n in range(400, 900):
    sys.stderr.write(str(n) + '\n')
    sys.stderr.flush()
    page = open_page(n).content
    get_tags(page)
