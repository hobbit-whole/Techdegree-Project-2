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
    names = ', '.join(names)
    #print(names)
    return names

def unpack_player_guardians():
    guardians = [d['guardians'] for d in player_info if 'guardians' in d]

    guardians = ', '.join(guardians)
    _names_of_guard = guardians.replace(" and", ",")
    #print(_names_of_guard)
    return _names_of_guard

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
    for i in range(0,len(player_info)):
        roster[i] = name[i], height[i], value[i], guardians[i]
    #print(roster)
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
            team_roster[j] += (random.choices(roster))

    #print(team_roster)
    return team_roster

def draft_team_players(game_time, team_number):
    team_players = game_time[team_number]
    player_name =  []
    player_height = []
    player_experience = []
    player_guardians = []

    #print(team_number)

    for i in range(1,len(team_players)):
        player_name.append(team_players[i][0])
        player_height.append(team_players[i][1])
        player_experience.append(team_players[i][2])
        player_guardians.append(team_players[i][3])


    return team_players, player_name, player_height, player_experience, player_guardians



def print_the_list(drafted_team):

    total_players = len(drafted_team[0])-1
    experienced_players = drafted_team[3].count('True')
    inexperienced_players = drafted_team[3].count('False')
    #height_in_int = drafted_team[2]
    #height = []
    


    average_height = round(statistics.mean(height),2)
    dashes = "-"*30
    
    '''print("\nNow Showing Stats For: {}\n\nStart of Data\n{}".format(drafted_team[0][0],dashes))

    print("Amount of Players: {}\nExperienced: {}\nInexperienced: {}\nAverage Height {} inches\n{}".format(total_players,experienced_players,inexperienced_players, average_height, dashes))

    print("Players on Team: \n\t{}".format(names))
    print("\nGuardians of Players: \n\t{}\n{}\nEnd of Data\n".format(_names, dashes))'''


if __name__ == "__main__":
    name = unpack_player_name()
    height = unpack_player_height()
    value = unpack_player_experience()
    guardians = unpack_player_guardians()
    #roster = create_dict(name, height, value, guardians)
    #team = teams()
    #game_time = random_sort(roster, team)

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

        
    print(value)

        

    

    