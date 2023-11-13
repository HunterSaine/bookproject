import requests

apikey = 'e9be841a2b734322476b32827df51230'

response = requests.get("https://api.the-odds-api.com/v4/sports/?apiKey=e9be841a2b734322476b32827df51230")

o = response.json()

