import requests
import json

apikey = 'e9be841a2b734322476b32827df51230'

response = requests.get("https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=e9be841a2b734322476b32827df51230&regions=us&markets=h2h,spreads&oddsFormat=american")
o = response.json() 


i = 0
while i < 15:
    k = o[i]
    j = k["bookmakers"]
    l = (j[1])
    z = 0
    while z < 12:
        l = (j[z])
        m = l["markets"]
        h2h = m[0]
        spread = m[1]
        ind = h2h["outcomes"]
        sp = spread["outcomes"]
        team_one_spread = sp[0]
        team_two_spread = sp[1]
        
        team_one_h2h = ind[0]
        team_two_h2h = ind[1]
        print(i,z)
        print(f"Sportsbook: {l["title"]}") 
        h2h["outcomes"] 
        
        print(f"Moneyline: {team_one_h2h["name"]} {team_one_h2h["price"]} vs {team_two_h2h["name"]} {team_two_h2h["price"]}")
        print(f"Spread: {team_one_spread["name"]} {team_one_spread["price"]} {team_one_spread["point"]} vs {team_two_spread["name"]} {team_two_spread["price"]} {team_two_spread["point"]}")

        print()
        z += 1
    i += 1
