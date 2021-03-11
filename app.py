from constants import TEAMS, PLAYERS
from collections import defaultdict
import random


if __name__ == "__main__":
    player_info = []
    team_info = []

    for player in PLAYERS:
        player_info.append(player)

    for team in TEAMS:
        team_info.append(team)


def unpack_player_name():
    names = [d['name'] for d in player_info if 'name' in d]
    #print(names)
    return names

def unpack_player_height():
    height = [d['height'] for d in player_info if 'height' in d]
    high = []
    for i in range(len(height)):
        high.append(height[i][0:2])
   # print(high)
    return high

def unpack_player_experience():
    experience = [d['experience'] for d in player_info if 'experience' in d]
    value = []
    for i in range(len(experience)): 
        if(experience[i] == 'YES'):
            experience[i] = 'True'
            value.append(experience[i])
        else:
            experience[i] = 'False'
            value.append(experience[i])
    #print(value)
    return(value)


def create_dict(name, height, value):

    roster = defaultdict(list)
    for i in range(0,len(player_info)):
        roster[i] = name[i] + ", " + height[i] + ", " + value[i]
   # print(roster)
    return roster


def teams():
    indie_team = {}
    for i in range(len(team_info)):
        indie_team[i] = team_info[i]
    #print(indie_team)
    return indie_team

def random_sort(roster, team):
    team_roster = defaultdict(list)
    max_team_people = int(len(player_info)/len(team_info))

    for j in range(0,len(team)):
        team_roster[j].append(team[j])

        for _ in range(0,max_team_people):
            team_roster[j] + (random.choices(roster))

    print(team_roster)
    return team_roster


name = unpack_player_name()
height = unpack_player_height()
value = unpack_player_experience()
roster = create_dict(name, height, value)
team = teams()

random_sort(roster, team)

