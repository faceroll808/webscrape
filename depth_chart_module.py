import page_loader


def get_first_team(short_name):
    return get_players(short_name, 0)


def get_second_team(short_name):
    return get_players(short_name, 1)


def get_first_and_second_team(short_name):
    return get_players(short_name, 0, 1)


def get_players(short_name, *indexes):
    doc = page_loader.load_depth_chart(short_name)
    rows = doc.find_all('tr', 'Table__TR Table__TR--sm Table__even')
    names = []
    for row in rows:
        players = row.find_all(class_="AnchorLink")
        if len(players) > 0:
            if 0 in indexes:
                names.append(players[0].text)
            if 1 in indexes:
                names.append(players[1].text)
    return names
