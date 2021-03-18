from constants import TEAMS, PLAYERS
from collections import defaultdict
import random, statistics

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

def unpack_player_guardians():

    _list_guardians = []

    guardians = [d['guardians'] for d in player_info if 'guardians' in d]

    guardians = ', '.join(guardians).replace(" and", ",")

    for item in guardians:
        item = guardians.split(', ')
        _list_guardians = item

    
    return _list_guardians

def unpack_player_height():
    height = [d['height'] for d in player_info if 'height' in d]
    high = []
    for i in range(0,len(height)):
        high.append(int(height[i][0:2]))

    #print(high)
    return high

def unpack_player_experience():
    experience = [d['experience'] for d in player_info if 'experience' in d]
    value = []
    for i in range(len(experience)): 
        if(experience[i] == 'YES'):
            experience[i] = True
            value.append(experience[i])
        else:
            experience[i] = False
            value.append(experience[i])
    #print(value)
    return(value)


def create_dict(name, height, value, guardians):

    roster = defaultdict(list)
    for i in range(int(len(player_info))):
        roster[i] = name[i], height[i], value[i]
    #print(len(player_info))
    return roster

    

def random_sort(roster):

    team_roster = []
    master_list = []

    while len(team_roster) < len(roster):
        master_list = random.choices(roster, k=len(roster))
        for i in range(0, len(roster)):
            if master_list[i] not in team_roster:
                team_roster.append(master_list[i])
    
    #print(team_roster)
    return team_roster

def assigned_to_team(roster_list):
    
    print(roster_list[0][2], team_info[0])
    length_player = int(len(roster_list)/len(team_info))
    _random_list = defaultdict(list)
    team = []

    #for i in range(0, len(team_info)):
    while j < 18:
        for j in range(0,18):
            if j <= 5 and j > 0:
                print(roster_list[j])
                if j < 11 and j >= 6:
                    print(roster_list[j])
                    if j < 18:
                        print(roster_list[j])


            



if __name__ == "__main__":
    name = unpack_player_name()
    height = unpack_player_height()
    value = unpack_player_experience()
    guardians = unpack_player_guardians()
    roster = create_dict(name, height, value, guardians)
    game_time = random_sort(roster)
    assigned_to_team(game_time)
    