import requests
from bs4 import BeautifulSoup


def load_page(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    return doc


def load_depth_chart(short_name):
    return load_page(f"https://www.espn.com/nba/team/depth/_/name/{short_name}/")


def load_main_team_page(short_name):
    return load_page(f"https://www.espn.com/nba/team/_/name/{short_name}/")


def load_team_player_stats_page(short_name):
    return load_page(f"https://www.espn.com/nba/team/stats/_/name/{short_name}/")


def load_nba_player_stats_page():
    return load_page("https://www.espn.com/nba/stats/player")


def load_todays_games():
    return load_page("https://www.espn.com/nba/scoreboard")
