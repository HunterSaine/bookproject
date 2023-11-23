import requests
import json

teamselect = input("Which team would you like info on? ")

apikey = 'e9be841a2b734322476b32827df51230'
apikeywgu ="b0deb1a32f7c45cb9785d4d1405b6a5a"
response = requests.get("https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=b0deb1a32f7c45cb9785d4d1405b6a5a&regions=us&markets=h2h,spreads&oddsFormat=american")

json_data = response.json() if response and response.status_code == 200 else None
formatted_json = json.dumps(json_data, indent=2) #format json response
#force quit if out of api responses
if len(formatted_json) < 5:     
    print("Out of API request. Please try again later")
    quit()

fanduel_info = ""
fanduel_h2h = ""
draftkings_info = ""
unibet_info = ''
print()
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
            elif json_data[i]["bookmakers"][j]['key'] == "unibet_us":
                unibet_info = json_data[i]["bookmakers"][j]["markets"]
            j += 1
    elif json_data[i]["away_team"] == teamselect :
        j = 0 
        while j < len(json_data[i]["bookmakers"]):
            #print(json_data[i]["bookmakers"][j])
            if json_data[i]["bookmakers"][j]['key'] == "fanduel":
                fanduel_info = json_data[i]["bookmakers"][j]["markets"]
            elif json_data[i]["bookmakers"][j]['key'] == "draftkings":
                draftkings_info = json_data[i]["bookmakers"][j]["markets"]
            elif json_data[i]["bookmakers"][j]['key'] == "unibet_us":
                unibet_info = json_data[i]["bookmakers"][j]["markets"]
            
            j += 1
    i += 1
try:
#fanduel variables
    fanduel_h2h = fanduel_info[0]
    fanduel_h2h_team1 = fanduel_h2h["outcomes"][0]
    fanduel_h2h_team2 = fanduel_h2h["outcomes"][1]
    fanduel_spread = fanduel_info[1]
    fanduel_spread_team1 = fanduel_spread["outcomes"][0]
    fanduel_spread_team2 = fanduel_spread["outcomes"][1]
#draftkings variables
    draftkings_h2h = draftkings_info[0]
    draftkings_h2h_team1 = draftkings_h2h["outcomes"][0]
    draftkings_h2h_team2 = draftkings_h2h["outcomes"][1]
    draftkings_spread = draftkings_info[1]
    draftkings_spread_team1 = draftkings_spread["outcomes"][0]
    draftkings_spread_team2 = draftkings_spread["outcomes"][1]
#unibet variables
    unibet_h2h = unibet_info[0]
    unibet_h2h_team1 = unibet_h2h["outcomes"][0]
    unibet_h2h_team2 = unibet_h2h["outcomes"][1]
    unibet_spread = unibet_info[1]
    unibet_spread_team1 = unibet_spread["outcomes"][0]
    unibet_spread_team2 = unibet_spread["outcomes"][1]
    if fanduel_h2h_team1["price"] >= 0:
        print("Fanduel Odds:")
        print("Moneyline: ")
        print(f'{fanduel_h2h_team1['name']} +{fanduel_h2h_team1['price']} ')
        print(f'{fanduel_h2h_team2['name']} {fanduel_h2h_team2['price']} ')
        print(f'Spread: {fanduel_spread_team1["name"]} +{fanduel_spread_team1["point"]} {fanduel_spread_team1['price']}')
        print(f'Spread: {fanduel_spread_team2["name"]} {fanduel_spread_team2["point"]} {fanduel_spread_team2['price']}')
        print()
    else:
        print("Fanduel Odds")
        print("Moneyline: ")
        print(f'{fanduel_h2h_team1['name']} {fanduel_h2h_team1['price']} ')
        print(f'{fanduel_h2h_team2['name']} +{fanduel_h2h_team2['price']} ')
        print(f'Spread: {fanduel_spread_team1["name"]} {fanduel_spread_team1["point"]} {fanduel_spread_team1['price']}') 
        print(f'Spread: {fanduel_spread_team2["name"]} +{fanduel_spread_team2["point"]} {fanduel_spread_team2['price']}') 

        print()   
    if draftkings_h2h_team1["price"] >= 0 :
        print("DraftKings Odds:")
        print("Moneyline: ")
        print(f'{draftkings_h2h_team1['name']} +{draftkings_h2h_team1['price']} ')
        print(f'{draftkings_h2h_team2['name']} {draftkings_h2h_team2['price']} ')
        print(f'Spread: {draftkings_spread_team1["name"]} +{draftkings_spread_team1["point"]} {draftkings_spread_team1['price']}')
        print(f'Spread: {draftkings_spread_team2["name"]} {draftkings_spread_team2["point"]} {draftkings_spread_team2['price']}')
        print('')
    else:
        print("Draftkings Odss:") 
        print("Moneyline: ")
        print(f'{draftkings_h2h_team1['name']} {draftkings_h2h_team1['price']} ')
        print(f'{draftkings_h2h_team2['name']} +{draftkings_h2h_team2['price']} ')
        print(f'Spread: {draftkings_spread_team1["name"]} {draftkings_spread_team1["point"]} {draftkings_spread_team1['price']}') 
        print(f'Spread: {draftkings_spread_team2["name"]} +{draftkings_spread_team2["point"]} {draftkings_spread_team2['price']}')
        print()
    #unibet
    if unibet_h2h_team1["price"] >= 0 :
        print("Unibet Odds:")
        print("Moneyline: ")
        print(f'{unibet_h2h_team1['name']} +{unibet_h2h_team1['price']} ')
        print(f'{unibet_h2h_team2['name']} {unibet_h2h_team2['price']} ')
        print(f'Spread: {unibet_spread_team1["name"]} +{unibet_spread_team1["point"]} {unibet_spread_team1['price']}')
        print(f'Spread: {unibet_spread_team2["name"]} {unibet_spread_team2["point"]} {unibet_spread_team2['price']}')
        print('')
    else:
        print("Unibet Odss:") 
        print("Moneyline: ")
        print(f'{unibet_h2h_team1['name']} {unibet_h2h_team1['price']} ')
        print(f'{unibet_h2h_team2['name']} +{unibet_h2h_team2['price']} ')
        print(f'Spread: {unibet_spread_team1["name"]} {unibet_spread_team1["point"]} {unibet_spread_team1['price']}') 
        print(f'Spread: {unibet_spread_team2["name"]} +{unibet_spread_team2["point"]} {unibet_spread_team2['price']}')
        print()

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