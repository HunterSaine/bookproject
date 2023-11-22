import requests
import json

apikey = 'e9be841a2b734322476b32827df51230'

response = requests.get("https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=e9be841a2b734322476b32827df51230&regions=us&markets=h2h,spreads&oddsFormat=american")


json_data = response.json() if response and response.status_code == 200 else None
formatted_json = json.dumps(json_data, indent=2) #format json response
#near_earth_objects = json_data["near_earth_objects"] #isoloate list of near earth objects

#f = open("sportslines.txt", "a")
#f.write(formatted_json)
#f.close()
fanduel_info = ""
fanduel_h2h = ""
draftkings_info = ""
teamselect = "Pittsburgh Steelers"
#input("Which team would you like info on? (example format: Pittsburgh Steelers)")
i = 0 
while i < len(json_data):
    if json_data[i]["home_team"] == teamselect  :
        j = 0 
        while j < len(json_data[i]["bookmakers"]):
            #print(json_data[i]["bookmakers"][j])
            if json_data[i]["bookmakers"][j]['key'] == "fanduel":
                fanduel_info = json_data[i]["bookmakers"][j]["markets"]
            elif json_data[i]["bookmakers"][j]['key'] == "draftkings":
                draftkings_info = json_data[i]["bookmakers"][j]["markets"]
            j += 1
    i += 1
#print(fanduel_info)
try:
    fanduel_h2h = fanduel_info[0]
    fanduel_h2h_team1 = fanduel_h2h["outcomes"][0]
    fanduel_h2h_team2 = fanduel_h2h["outcomes"][1]
    fanduel_spread = fanduel_info[1]
    fanduel_spread_team1 = fanduel_spread["outcomes"][0]
    fanduel_spread_team2 = fanduel_spread["outcomes"][1]
#print(fanduel_h2h_team1)
    if fanduel_h2h_team1["price"] >= 0:
        print("Fanduel Odds:")
        print(f'{fanduel_h2h_team1['name']} +{fanduel_h2h_team1['price']} ')
        print(f'{fanduel_h2h_team2['name']} {fanduel_h2h_team2['price']} ')
        print(f'Spread: {fanduel_spread_team1["name"]} +{fanduel_spread_team1["point"]} {fanduel_spread_team1['price']}')
        print(f'Spread: {fanduel_spread_team2["name"]} {fanduel_spread_team2["point"]} {fanduel_spread_team2['price']}')
        print('')

    else:
        print("Fanduel Odds")
        print(f'{fanduel_h2h_team1['name']} {fanduel_h2h_team1['price']} ')
        print(f'{fanduel_h2h_team2['name']} +{fanduel_h2h_team2['price']} ')
        print(f'{fanduel_spread_team1["name"]} +{fanduel_spread_team1["point"]} {fanduel_spread_team1['price']}')

    
except:
    print("Error: Enter valid team. Format ex. Miami Dolphins")




i = 0
while i < len(json_data):
    if json_data[i]["away_team"] == teamselect  :
        j = 0 
        while j < len(json_data[i]["bookmakers"]):
            #print(json_data[i]["bookmakers"][j])
            if json_data[i]["bookmakers"][j]['key'] == "fanduel":
                fanduel_info = json_data[i]["bookmakers"][j]["markets"]
            elif json_data[i]["bookmakers"][j]['key'] == "draftkings":
                draftkings_info = json_data[i]["bookmakers"][j]["markets"]
            j += 1
    i += 1

#print(fanduel_info)

#print(json_data[0]["bookmakers"][0]["key"])
#i = 0
#while i < 15:
#    k = o[i]
#    j = k["bookmakers"]
#    l = (j[1])
#    z = 0
#    while z < 1:
#        l = (j[z])
#        m = l["markets"]
#        h2h = m[0]
#        spread = m[1]
#        ind = h2h["outcomes"]
#        sp = spread["outcomes"]
#        team_one_spread = sp[0]
#        team_two_spread = sp[1]
#        
#        team_one_h2h = ind[0]
#        team_two_h2h = ind[1]
#        f = open("sportslines.txt")
#        #f.write(i,z)
#    f.write(f"Spread: {team_one_spread["name"]} {team_one_spread["price"]} {team_one_spread["point"]} vs {team_two_spread["name"]} {team_two_spread["price"]} {team_two_spread["point"]}")
#
#        f.write()
#        z += 1
#    i += 1
