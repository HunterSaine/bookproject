import requests
import json

apikey = 'e9be841a2b734322476b32827df51230'

response = requests.get("https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=e9be841a2b734322476b32827df51230&regions=us&markets=h2h,spreads&oddsFormat=american")
o = response.json() 
firstkey = o[1]
k = (firstkey["bookmakers"])
print(k)
h = k[1]
print(h["key"]) 
