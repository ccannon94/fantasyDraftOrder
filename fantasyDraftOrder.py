import os
from random import shuffle
from espn_api.football import League

swid = os.environ.get('swid')
espn_s2 = os.environ.get('espn_s2')

league = League(league_id=325751, year=2024, swid=swid, espn_s2=espn_s2)

teams:list = league.teams

for i in range(100000):
    shuffle(teams)


for team in teams:
    print(team.team_name.strip())