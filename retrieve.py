import requests
import json

apiKey = "e9be841a2b734322476b32827df51230"
response = requests.get("https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=e9be841a2b734322476b32827df51230&regions=us&markets=h2h,spreads&oddsFormat=american")
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["id"]:
    print(result["home_team"])
