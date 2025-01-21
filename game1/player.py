import requests
import time
from urllib.parse import quote
# Convert epoch timestamp to a human-readable UNIX format
def epoch_to_unix(epoch_timestamp):
    struct_time = time.localtime(epoch_timestamp)
    unix_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
    return unix_time

base_url="https://api.opendota.com/api/"
class Player:
    def __init__(self, account_id):
        self.account_id=account_id
    
    def get_player_data(self):
        url=base_url+"players/"+str(self.account_id)
        self.data=requests.get(url).json()

    def get_player_wl(self):
        url=base_url+"players/"+str(self.account_id)+"/wl"
        self.wl=requests.get(url).json()

    def get_player_matches(self):
        # url=base_url+"players/"+str(self.account_id)+"/matches"
        query=f'''SELECT player_matches.hero_id,player_matches.hero_damage,player_matches.tower_damage,player_matches.hero_healing,player_matches.gold_per_min,player_matches.xp_per_min,player_matches.kills,player_matches.deaths,player_matches.assists,matches.*
        FROM player_matches
        JOIN matches
        ON player_matches.match_id = matches.match_id
        WHERE player_matches.account_id = {self.account_id} Limit 100;'''
        url=base_url+"explorer?sql="+quote(query)
        print(url)
        self.matches=requests.get(url).json().get('rows')
        for i in range(len(self.matches)):
            try:
                self.matches[i]['kd']=round(self.matches[i]['kills']/self.matches[i]['deaths'],3)
            except ZeroDivisionError:
                self.matches[i]['kd']="INF"
            self.matches[i]['start_time']=epoch_to_unix(self.matches[i]['start_time'])
            self.matches[i]['color']="positive" if self.matches[i]['radiant_win'] else "negative"

    def get_player_recent_matches(self):
        url=base_url+"players/"+str(self.account_id)+"/recentMatches"
        self.recent_matches=requests.get(url).json()
    
    def get_player_heroes(self):
        url=base_url+"players/"+str(self.account_id)+"/heroes"
        self.heroes=requests.get(url).json()
    
    def get_player_peers(self):
        url=base_url+"players/"+str(self.account_id)+"/peers"
        self.peers=requests.get(url).json()
        
    def get_player_ratings(self):
        url=base_url+"players/"+str(self.account_id)+"/ratings"
        self.ratings=requests.get(url).json()
    
    def fetch_player_data(self):
        self.get_player_data()
        self.get_player_wl()
        self.get_player_matches()
        self.get_player_recent_matches()
        self.get_player_heroes()
        self.get_player_peers()
        self.get_player_ratings()
        return {
            "data":self.data,
            "wl":self.wl,
            "matches":self.matches,
            "recent_matches":self.recent_matches,
            "heroes":self.heroes,
            "peers":self.peers,
            "ratings":self.ratings
        }
    def fetch_player_data_specific(self,specific_attr):
        if specific_attr=="data":
            self.get_player_data()
            return self.data
        elif specific_attr=="wl":
            self.get_player_wl()
            return self.wl
        elif specific_attr=="matches":
            self.get_player_matches()
            return self.matches
        elif specific_attr=="recent_matches":
            self.get_player_recent_matches()
            return self.recent_matches
        elif specific_attr=="heroes":
            self.get_player_heroes()
            return self.heroes
        elif specific_attr=="peers":
            self.get_player_peers()
            return self.peers
        elif specific_attr=="ratings":
            self.get_player_ratings()
            return self.ratings
        else:
            return "Invalid attribute"