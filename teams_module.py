# {short_name, mascot}
all_teams = {
    'bos': ["Boston", "Celtics"],
    'bkn': ["Brooklyn", "Nets"],
    'ny': ["New York", "Knicks"],
    'phi': ["Philadelphia", "76ers"],
    'tor': ["Toronto", "Raptors"],
    'den': ["Denver", "Nuggets"],
    'min': ["Minnesota", "Timberwolves"],
    'okc': ["Oklahoma City", "Thunder"],
    'por': ["Portland", "Trail Blazers"],
    'utah': ["Utah", "Jazz"],
    'chi': ["Chicago", "Bulls"],
    'cle': ["Cleveland", "Cavaliers"],
    'det': ["Detroit", "Pistons"],
    'ind': ["Indiana", "Pacers"],
    'mil': ["milwaukee", "Bucks"],
    'gs': ["Golden State", "Warriors"],
    'lac': ["Los Angeles", "Clippers"],
    'lal': ["Los Angeles", "Lakers"],
    'phx': ["Phoenix", "Suns"],
    'sac': ["Sacramento", "Kings"],
    'atl': ["Atlanta", "Hawks"],
    'cha': ["Charlotte", "Hornets"],
    'mia': ["Miami", "Heat"],
    'orl': ["Orlando", "Magic"],
    'wsh': ["Washington", "Wizards"],
    'dal': ["Dallas", "Mavericks"],
    'hou': ["Houston", "Rockets"],
    'mem': ["Memphis", "Grizzlies"],
    'no': ["New Orleans", "Pelicans"],
    'sa': ["San Antonio", "Spurs"],
}


def get_city(short_name):
    return all_teams.get(short_name)[0]


def get_mascot(short_name):
    return all_teams.get(short_name)[1]


def get_full_name(short_name):
    return f"{get_city(short_name)} {get_mascot(short_name)}"


def get_short_name_from_mascot(mascot):
    for short_name in all_teams:
        if all_teams.get(short_name)[1] == mascot:
            return short_name


def get_short_name_from_city(city):
    for short_name in all_teams:
        if all_teams.get(short_name)[0] == city:
            return short_name
