import sqlite3
try:
    connection = sqlite3.connect("fantasy_cricket.db")
except sqlite3.OperationalError:
    print("Cant connect to database")

cursor = connection.cursor()
data = cursor.execute("SELECT PlayerID,Player,Value,Ctg FROM stats")
players_stats = cursor.fetchall()

batsman = []
bowlers = []
all_rounder = []
wicket_keeper = []
name_value = {}
final_team_list = []
open_team_players=[]
match_list = []
team_names = []
current_match_data = {}
selected_player_data = {}
final_team_with_points ={}

for i in players_stats:
    if i[3] == "BAT":
        batsman.append(i[1])
    if i[3] == "WK":
        wicket_keeper.append(i[1])
    if i[3] == "AR":
        all_rounder.append(i[1])
    if i[3] == "BWL":
        bowlers.append(i[1])
for i in players_stats:
    name_value[i[1]]=i[2]

def add_team_database(team_name):
    for i in final_team_list:
        players_to_add = (str(team_name), i, name_value[i])
        cursor.execute("INSERT OR IGNORE INTO teams(Name,Players,Value) Values(?,?,?)",  players_to_add)
        connection.commit()
def refresh_category_list():
    batsman.clear()
    bowlers.clear()
    all_rounder.clear()
    wicket_keeper.clear()
    final_team_list.clear()
    for i in players_stats:
        if i[3] == "BAT":
            batsman.append(i[1])
        if i[3] == "WK":
            wicket_keeper.append(i[1])
        if i[3] == "AR":
            all_rounder.append(i[1])
        if i[3] == "BWL":
            bowlers.append(i[1])



def get_team_names():
    team_names.clear()
    teams = cursor.execute("SELECT Name, Players, Value FROM teams")
    all_teams = teams.fetchall()

    i = 0
    while i < len(all_teams):
        team_names.append(all_teams[i][0])
        i += 11
    return team_names


def get_selected_team(name):
    open_team_players.clear()
    open = cursor.execute("SELECT Players,Value From teams WHERE Name=?", (name,))
    open_team = open.fetchall()
    for i in open_team:
        open_team_players.append(i)
def get_match_list():
    match_list.clear()
    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for name in res:
        match_list.append(name[0])
    match_list.remove("stats")
    match_list.remove("teams")

def data_for_calculation(match):
    details = cursor.execute(f"SELECT Player,Scored,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RO,Faced From {match}")
    match_data = details.fetchall()

    for i in match_data:
        current_match_data[i[0]] = {"Scored":i[1],"Fours":i[2],"Sixes":i[3],"Bowled":i[4],"Maiden":i[5],"Given": i[6],"Wkts": i[7],
                                    "Catches": i[8], "Stumping":i[9],"RO": i[10],"Faced":i[11]}
data_for_calculation("match")
print(current_match_data)




















