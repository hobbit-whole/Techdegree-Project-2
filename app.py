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

    #print(indie_team)

    while len(team_roster) < len(roster):
        master_list = random.choices(roster, k=len(roster))
        for i in range(0, len(roster)):
            if master_list[i] not in team_roster:
                team_roster.append(master_list[i])
    
    print(team_roster)
    return team_roster



if __name__ == "__main__":
    name = unpack_player_name()
    height = unpack_player_height()
    value = unpack_player_experience()
    guardians = unpack_player_guardians()
    roster = create_dict(name, height, value, guardians)
    game_time = random_sort(roster)

    '''continuing_on = ''
    while continuing_on.lower() != 'n':

        team_number = ''
        while team_number not in range(0,3):
            try:
                team_number = int(input("\n1) Panthers \n2) Bandits  \n3) Warriors\n \nPick a Team: "))-1
            except ValueError:
                print('Please enter number 1, 2, or 3')

        drafted_team = draft_team_players(game_time, team_number)
    
        print_the_list(drafted_team)
        continuing_on = input("\nWould you like to get stats [y/n]: ")
        if(continuing_on == 'n'):
            print("Good Bye")'''
    