import page_loader
import teams_module


def get_last_five(short_name):
    doc = page_loader.load_main_team_page(short_name)

    results = doc.find_all("span", "Schedule__Result")
    scores = doc.find_all("span", "Schedule__Score")

    total_scored = 0
    total_against = 0

    for i in range(5):
        s = scores[i].text.split("-")
        if results[i].text == "L":
            total_scored += int(s[1])
            total_against += int(s[0])
        else:
            total_scored += int(s[0])
            total_against += int(s[1])
    return [total_scored, total_against]


def get_todays_matches():
    matches = []
    doc = page_loader.load_todays_games()
    comp = doc.find_all("ul", "ScoreboardScoreCell__Competitors")
    for c in comp:
        match = []
        teams_playing = c.find_all("div", "ScoreCell__TeamName")
        for team in teams_playing:
            match.append(teams_module.get_short_name_from_mascot(team.text))
        matches.append(match)
    return matches
