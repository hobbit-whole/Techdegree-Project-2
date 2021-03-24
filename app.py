from constants import TEAMS, PLAYERS
from collections import defaultdict
import random, statistics

player_info = []
team_info = []



def unpack_player_name(player_info):
    names = [d['name'] for d in player_info if 'name' in d]
    #print(names)
    return names

def unpack_player_guardians(player_info):
    guardians = [d['guardians'] for d in player_info if 'guardians' in d]

    #print(guardians)
    return(guardians)


def unpack_player_height(player_info):
    height = [d['height'] for d in player_info if 'height' in d]
    high = []
    for i in range(0,len(height)):
        high.append(int(height[i][0:2]))

    #print(high)
    return high

def unpack_player_experience(player_info):
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


def create_dict(player_info, name, height, value, guardians):

    roster = defaultdict(list)

    for i in range(int(len(player_info))):
        roster[i] = name[i], height[i], value[i], guardians[i]
    return roster

def populate_team(roster_list):

    team_roster = []
    master_list = []


    while len(team_roster) < len(roster_list):
        master_list = random.choices(roster, k=len(roster_list))
        for i in range(0, len(roster_list)):
            if master_list[i] not in team_roster:
                team_roster.append(master_list[i])

    return team_roster

def assigned_to_team(roster_list, team_info):

    team = defaultdict(list)
    picked_player= []
    temp_player_list = []

    for i in range(len(roster_list)):
        picked_player.append(roster_list[i])

    for j in range(len(team_info)):
            team[j].append(team_info[j])
    j = 0
    i = 0
    
    
    for i in range(len(picked_player)):
        for j in range(len(team)):
            experience = 0
            inexperience = 0
            
            while len(team[j]) < 7 and len(picked_player) > 0:
                if experience < 3 and picked_player[i][2] == True:          
                    team[j].append(picked_player.pop(i))
                    experience += 1  

                elif inexperience < 3 and picked_player[i][2] == False:          
                    team[j].append(picked_player.pop(i))
                    inexperience += 1  

                else:
                    temp_player_list.append(picked_player.pop(i))

            while len(temp_player_list) > 0:
                team[2].append(temp_player_list.pop(i))

    #print(team)
    return team



if __name__ == "__main__":
    for player in PLAYERS:
        player_info.append(player)

    for team in TEAMS:
        team_info.append(team)

    name = unpack_player_name(player_info)
    height = unpack_player_height(player_info)
    value = unpack_player_experience(player_info)
    guardians = unpack_player_guardians(player_info)
    roster = create_dict(player_info, name, height, value, guardians)
    roster_list = populate_team(roster)
    sorted_roster = assigned_to_team(roster_list, team_info)

    menu_response = 0
    dashes = "-"
    _continue_choice = ''

    while menu_response != 1 and menu_response != 2:
        
        print('\nBASKETBALL TEAM STATS TOOL')

        print('\n{}MENU{}'.format(dashes*10, dashes*10))

        
        try:
            menu_response = int(input('\nHere are your choices\n\n 1) Display Team Stats\n 2) Quit\n\nEnter in an option: '))
        except ValueError:
            print('Please choose between 1 and 2')
                
        except NameError:
            print('Please choose between 1 and 2')
        
        if menu_response > 2 or menu_response < 1:
            print('Please enter in a 1 or 2')


        while menu_response == 1 and _continue_choice.lower() != 'n':  
            try:  
                team_number = int(input('\nHere are the teams\n\n 1) Panthers\n 2) Bandits\n 3) warriors\n\nEnter in an option:  '))


                if team_number <= 3 and team_number != 0:
                    print('{}\nYou selected: {}\n'.format(dashes*25, sorted_roster[team_number-1][0]))
                    print('Total Players: {}'.format(len(sorted_roster[team_number-1])-1))
                

                    experience = 0
                    inexperience = 0
                    for i in range(1, len(sorted_roster[team_number-1])):
                        if sorted_roster[team_number-1][i][2] == True:
                            experience += 1
                        else:
                            inexperience += 1

                    print('Experienced Players: {}'.format(experience))
                    print('Inexperienced Player: {}'.format(inexperience))



                    _list_of_height = []
                    for i in range(1, len(sorted_roster[team_number-1])):
                        height_list = []
                        height_list.append(sorted_roster[team_number-1][i])
                        for z in range(len(height_list)):
                            _list_of_height.append(height_list[z][1])
                    _average_player = round(statistics.mean(_list_of_height), 1)
                    print('Average Height: {} inches\n{}'.format(_average_player, dashes*25))

                    names = []
                    for i in range(1, len(sorted_roster[team_number-1])):
                        names.append(sorted_roster[team_number-1][i][0])
                        names_of_players = ', '.join(names)
                    print('Players on the team :\n\t{}\n'.format(names_of_players))

                    guardian_for_player = []
                    for i in range(1, len(sorted_roster[team_number-1])):
                        guardian_for_player.append(sorted_roster[team_number-1][i][3])
                        names_of_guardians = ', '.join(guardian_for_player).replace(" and", ",")           
                    print('Guardians: \n\t{}\n'.format(names_of_guardians))

            except ValueError:
                print('Please enter in a number 1-3')
                
            except NameError:
                print('Please enter in a number between 1-3')

            
            _continue_choice = input('{}\nWould you like to pick another team (y/n): '.format(dashes*25))
            if _continue_choice.lower() == 'n':
                break
            menu_response = 0
    
    else:
        print('{}\nExiting Program \n'.format(dashes*25))


        
        
        
