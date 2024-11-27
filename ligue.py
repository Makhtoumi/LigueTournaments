import csv 
import itertools
import random

def write_to_csv(file_pathe, headers, data,data_2):
    with open(file_pathe, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)
        writer.writerow([])
        for row in data_2:
            writer.writerow(row)
file_pathe = 'liga.csv'
headers = ['Teams', 'Points', 'Victoires', 'Nuls', 'Défaites', 'Buts Marqués', 'Buts Encaissés', 'Différence de Buts','moyenne de but']
def read_from_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(tuple(row))
    return data
file_path = 'teams_list.csv'  
teams = read_from_csv(file_path)
random.shuffle(teams)

standings = {team: 0 for team in teams}
gols = {team: 0 for team in teams}
kblou = {team: 0 for team in teams}
victoir = {team: 0 for team in teams}
nul = {team: 0 for team in teams}
defait = {team: 0 for team in teams}
matches = list(itertools.combinations(teams, 2))
num_rounds = len(teams) - 1
matches_dict = {}
match_finale = []
Y=[]
dict_finale ={}

for round_num in range(num_rounds):
    group1 = teams[:len(teams)//2]
    group2 = teams[len(teams)//2:]
    
    matches = list(zip(group1, group2[::-1]))
    
    matches_dict[round_num+1] = matches 
    
    teams.insert(1, teams.pop())

for i in range(2):
    round_scores = [0] * len(teams)
    for round in matches_dict:
        print(round)
        for match in matches_dict[round]:
            home_team = match[0]
            away_team = match[1]
            while True:
                try:
                    if i ==1 :
                        home_score = int(input("Enter the score for {} vs {}: ".format(home_team, away_team)))
                        away_score = int(input("Enter the score for {} vs {}: ".format(away_team, home_team)))
                    else:
                        away_score = int(input("Enter the score for {} vs {}: ".format(away_team, home_team)))
                        home_score = int(input("Enter the score for {} vs {}: ".format(home_team, away_team)))
                        
                    break
                except ValueError:
                    print("invalid input. please enter a number")
            if home_score > away_score:
                standings[home_team] += 3
                victoir[home_team] +=1
                defait[away_team] +=1
            elif away_score > home_score:
                standings[away_team] += 3
                victoir[away_team] += 1
                defait[home_team] += 1
            else:
                standings[home_team] += 1
                standings[away_team] += 1
                nul[home_team] += 1
                nul[away_team] += 1 
            gols[home_team] += home_score
            gols[away_team] += away_score
            kblou[home_team] += away_score
            kblou[away_team] += home_score
            
            X = [home_team,home_score,away_score,away_team]
            match_finale.append(X)
        sorted_items = sorted(standings.items(), key=lambda x:(x[1],gols[x[0]]-kblou[x[0]],gols[x[0]]), reverse=True)
        print(sorted_items)
            
standings_list = []
for team, points  in sorted(standings.items(), key=lambda x:(x[1],gols[x[0]]-kblou[x[0]],gols[x[0]]), reverse=True):
    sl = [team, points,victoir[team],nul[team],defait[team],gols[team],kblou[team] , gols[team]-kblou[team]]
    standings_list.append(sl)

write_to_csv(file_pathe, headers, standings_list,Y)
