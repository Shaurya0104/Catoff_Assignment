import requests
from urllib.parse import quote

query='''SELECT player_matches.kills,player_matches.deaths,player_matches.assists,matches.*
FROM player_matches
JOIN matches
ON player_matches.match_id = matches.match_id
WHERE player_matches.account_id = 1296625;'''
print(quote(query))
url="https://api.opendota.com/api/explorer?sql="+quote(query)
response=requests.get(url)
print(response.json().get("rows")[0])

