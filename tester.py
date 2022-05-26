import schedule_module
import stats_module
import depth_chart_module
import teams_module

# matches = schedule_module.get_todays_matches()
# print(matches)
#
# match = matches[0]
# print(match)
#
# depth_chart = depth_chart_module.get_first_and_second_team("chi")
# print(depth_chart)
#
# player_stats = stats_module.get_team_player_stats("chi")
# print(player_stats)
#
# total = 0
# for player in depth_chart:
#     print(f"{player_stats.get(player).get('name')} - {player_stats.get(player).get('PTS')}")
#     total += float(player_stats.get(player).get('PTS'))
#
# last_five = schedule_module.get_last_five("chi")
# print(last_five)
#
# scored_avg = last_five[0]/5
# print(scored_avg)
#
# print((scored_avg + total) / 2)











matches = schedule_module.get_todays_matches()

match = matches[0]
road = match[0]
home = match[1]
print(f"{road} @ {home}")
print(f"{teams_module.get_full_name(road)} @ {teams_module.get_full_name(home)}")

last_five_road = schedule_module.get_last_five(road)
print(last_five_road)
last_five_home = schedule_module.get_last_five(home)
print(last_five_home)


print()
print(teams_module.get_full_name (road))
depth_chart = depth_chart_module.get_first_and_second_team(road)
stats = stats_module.get_team_player_stats(road)





for player in depth_chart:
    try:
        player_stats = stats.get(player)
        print(f"{player_stats.get('name')} - {player_stats.get('PTS')}")
    except:
        print(f"Error on {player}")

print()
print(teams_module.get_full_name(home))
depth_chart = depth_chart_module.get_first_and_second_team(home)
stats = stats_module.get_team_player_stats(home)
for player in depth_chart:
    try :
        player_stats = stats.get(player)
        print(f"{player_stats.get('name')} - {player_stats.get('PTS')}")
    except:
        print(f"Error on {player}")

