
import requests
import json
import time

def get_bov_games():
    "Retrieves json object with all games on bov. with live betting"
    base_url = "https://sports.bovada.lv/services/sports/event/events/under/A/next?status=O&status=H&status=U&status=C&maxHours=24&liveOnly=true"
    r = requests.get(base_url)
    return json.loads(r.text)

def get_nba_games():
    "Retrieves all nba games with live betting"
    all_games_list = get_bov_games()['items']
    nba_games = [game for game in all_games_list if(game['type']=='NBA')]
    return nba_games

def get_next_nba_game_ids():
    "Get all game ids in 24hr window"
    nba_games = get_nba_games()
    game_ids = [int(game['id']) for game in nba_games]
    return game_ids

def get_live_nba_game_ids():
    "Get all game ids in 24hr window"
    nba_games = get_nba_games()
    curr_time = time.time()
    game_ids = [int(game['id']) for game in nba_games if(game['startTime'] < curr_time)]
    return game_ids
