import page_loader


def get_all_player_stats():
    pass


def get_team_player_stats(short_name):
    doc = page_loader.load_team_player_stats_page(short_name)

    stat_titles = []
    headers = doc.find_all("th", "tar stats-cell Table__TH")
    for header in headers:
        stat_titles.append(header)

    rows = doc.find_all("tr", "Table__TR Table__TR--sm Table__even")
    players_by_id = {}
    max_id = 0
    for row in rows:
        # print(row)
        player = row.find("a")
        if player is not None:
            players_by_id[row.attrs['data-idx']] = {'name': player.text}
        elif row.text == "Total":
            players_by_id[row.attrs['data-idx']] = {'name': 'Total'}
            max_id = row.attrs['data-idx']
        else:
            # print()
            stats = row.find_all("span")
            if len(stats) > 2:
                id = row.attrs['data-idx']
                all_stats = {}
                for i in range(len(stat_titles)):
                    try:
                        all_stats.update({stat_titles[i].text: stats[i].text})
                    except IndexError:
                        break
                players_by_id[id].update(all_stats)
                if row.attrs['data-idx'] == max_id:
                    break
    players_by_name = {}
    for player in players_by_id.values():
        players_by_name.update({player.get('name'): player})
    return players_by_name
