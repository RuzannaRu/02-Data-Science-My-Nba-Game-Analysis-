import csv
from statistic_reg import table
from print_data import print_nba_stats

def load_data(filename):
    res = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter= '|')
        for row in csvreader: res.append(row)
    return res
players_data = []

def set_players_data(play_by_play_moves):
    for play in play_by_play_moves:
        if len(table(play[7])) > 0:
            for data in table(play[7]):
                player_name = data[0][1]
                point_field = data[1]
                if player_name not in [i['player_name'] for i in players_data]:
                    players_data.append(
                        {'player_name': player_name, 'FG': 0, 'FGA': 0, 'FG%': 0, '3P': 0, '3PA': 0, '3P%': 0, 'FT': 0,
                         'FTA': 0, 'FT%': 0, 'ORB': 0,'DRB': 0, 'TRB': 0, 'AST': 0, 'STL': 0, 'BLK': 0, 'TOV': 0,
                         'PF': 0, 'PTS': 0})
                index = [players_data.index(i) for i in players_data if i['player_name'] == player_name][0]
                players_data[index][point_field] += 1
                if point_field not in ('STL', 'BLK', 'PF'):
                    players_data[index]['is_home_team'] = play[2] == play[4]
                else: players_data[index]['is_home_team'] = play[2] != play[4]


def calculation(players_data):
    for player in players_data:
        player['3PA'] += player['3P']; player['FGA'] += player['FG']; player['FGA'] += player['3PA']
        player['FG'] += player['3P']; player['FTA'] += player['FT']; player['TRB'] = player['ORB'] + player['DRB']
        player['FG%'] = "{:.3f}".format(round(player['FG'] / player['FGA'], 3)) if player['FGA'] != 0 else 0
        player['FT%'] = "{:.3f}".format(round(player['FT'] / player['FTA'], 3)) if player['FTA'] != 0 else 0
        player['3P%'] = "{:.3f}".format(round(player['3P'] / player['3PA'], 3)) if player['3PA'] != 0 else 0
        player['PTS'] = 2 * (player['FG'] - player['3P']) + 3 * player['3P'] + player['FT']




set_players_data(load_data('nba_game_warriors_thunder_20181016.txt'))
calculation(players_data)
AWAY_TEAM = load_data('nba_game_warriors_thunder_20181016.txt')[0][3]
HOME_TEAM = load_data('nba_game_warriors_thunder_20181016.txt')[0][4]
result = {'home_team': {'name': HOME_TEAM, 'players_data': []}, 'away_team': {'name': AWAY_TEAM, 'players_data': []}}
for i in players_data:
    if i['is_home_team']: result['home_team']['players_data'].append(i)
    else: result['away_team']['players_data'].append(i)

print_nba_stats(result['home_team'])
print()
print_nba_stats(result['away_team'])