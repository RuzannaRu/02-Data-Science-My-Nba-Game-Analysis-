def _(value):
    return (6-len(str(value)))*' '

# def print_nba_stats(team_dict):
#     total = {'FG': 0, 'FGA': 0, 'FG%': 0, '3P': 0, '3PA': 0, '3P%': 0, 'FT': 0, 'FTA': 0, 'FT%': 0, 'ORB': 0, 'TRB': 0, 'AST': 0, 'STL': 0, 'BLK': 0, 'TOV': 0, 'PF': 0, 'PTS': 0}
#     print('Players         FG      FGA      FG%       3P      3PA      3P%      FT      FTA      FT%      ORB      TRB      AST      STL      BLK      TOV      PF      PTS')
#     for gmr in team_dict['players_data']:
#         space = (16-len(gmr['player_name']))*' '
#         # print(f"{gmr['player_name']}{space}{gmr['FG']}{_(gmr['FG'])}{gmr['FGA']}{_(gmr['FGA'])}{gmr['FG%']}{_(gmr['FG%'])})")
#         print(f"{gmr['player_name']}{space}{gmr['FG']}{_(gmr['FG'])}{gmr['FGA']}{_(gmr['FGA'])}{gmr['FG%']}{_(gmr['FG%'])}{gmr['3P']}{_(gmr['3P'])}{gmr['3PA']}{_(gmr['3PA'])}{gmr['3P%']}{_(gmr['3P%'])}{gmr['3P%']}{_(gmr['3P%'])}{gmr['FT']}{_(gmr['FT'])}{gmr['FTA']}{_(gmr['FTA'])}{gmr['FT%']}{_(gmr['FT%'])}{gmr['ORB']}{_(gmr['ORB'])}{gmr['TRB']}{_(gmr['TRB'])}{gmr['AST']}{_(gmr['AST'])}{gmr['STL']}{_(gmr['STL'])}{gmr['BLK']}{_(gmr['BLK'])}{gmr['TOV']}{_(gmr['TOV'])}{gmr['PF']}{_(gmr['PF'])}{gmr['PTS']}{_(gmr['PTS'])}")
#
#         for feature in total.keys():
#             total[feature] += float(gmr[feature])
#     print('Team Totals  ', end='   ')
#     for num in total.values():
#         if list(total.values()).index(num) not in (2, 5, 8): print(int(num), end=_(int(num)))
#         else: print(float("{:.2f}".format(num)), end=_(float("{:.2f}".format(num))))




#
# def print_nba_stats(team_dict):
#     total = {'FG': 0, 'FGA': 0, 'FG%': 0, '3P': 0, '3PA': 0, '3P%': 0, 'FT': 0, 'FTA': 0, 'FT%': 0, 'ORB': 0, 'TRB': 0, 'AST': 0, 'STL': 0, 'BLK': 0, 'TOV': 0, 'PF': 0, 'PTS': 0}
#     print('Players         FG      FGA      FG%       3P      3PA      3P%      FT      FTA      FT%      ORB      TRB      AST      STL      BLK      TOV      PF      PTS')
#     for gmr in team_dict['players_data']:
#         space = (16-len(gmr['player_name']))*' '
#         print(f"{gmr['player_name']}{space}{gmr['FG']}{_(gmr['FG'])}{gmr['FGA']}{_(gmr['FGA'])}{gmr['FG%']}{_(gmr['FG%'])}{gmr['3P']}{_(gmr['3P'])}{gmr['3PA']}{_(gmr['3PA'])}{gmr['3P%']}{_(gmr['3P%'])}{gmr['FT']}{_(gmr['FT'])}{gmr['FTA']}{_(gmr['FTA'])}{gmr['FT%']}{_(gmr['FT%'])}{gmr['ORB']}{_(gmr['ORB'])}{gmr['TRB']}{_(gmr['TRB'])}{gmr['AST']}{_(gmr['AST'])}{gmr['STL']}{_(gmr['STL'])}{gmr['BLK']}{_(gmr['BLK'])}{gmr['TOV']}{_(gmr['TOV'])}{gmr['PF']}{_(gmr['PF'])}{gmr['PTS']}{_(gmr['PTS'])}")
#
#         for feature in total.keys():
#             total[feature] += float(gmr[feature])
#     print('Team Totals  ', end='   ')
#     for num in total.values():
#         if list(total.values()).index(num) not in (2, 5, 8):
#             print(int(num), end=_(int(num)))
#         else:
#             print(float("{:.2f}".format(num)), end=_(float("{:.2f}".format(num))))


def print_nba_stats(team_dict):
    total = {'FG': 0, 'FGA': 0, 'FG%': 0, '3P': 0, '3PA': 0, '3P%': 0, 'FT': 0, 'FTA': 0, 'FT%': 0, 'ORB': 0, 'TRB': 0, 'AST': 0, 'STL': 0, 'BLK': 0, 'TOV': 0, 'PF': 0, 'PTS': 0}
    print('Players                 FG      FGA      FG%       3P      3PA      3P%      FT      FTA      FT%      ORB      TRB      AST      STL      BLK      TOV      PF      PTS')
    for gmr in team_dict['players_data']:
        space = (20 - len(gmr['player_name'])) * ' '
        print(f"{gmr['player_name']}{space}{gmr['FG']}{_(gmr['FG'])}{gmr['FGA']}{_(gmr['FGA'])}{gmr['FG%']}{_(gmr['FG%'])}{gmr['3P']}{_(gmr['3P'])}{gmr['3PA']}{_(gmr['3PA'])}{gmr['3P%']}{_(gmr['3P%'])}{gmr['FT']}{_(gmr['FT'])}{gmr['FTA']}{_(gmr['FTA'])}{gmr['FT%']}{_(gmr['FT%'])}{gmr['ORB']}{_(gmr['ORB'])}{gmr['TRB']}{_(gmr['TRB'])}{gmr['AST']}{_(gmr['AST'])}{gmr['STL']}{_(gmr['STL'])}{gmr['BLK']}{_(gmr['BLK'])}{gmr['TOV']}{_(gmr['TOV'])}{gmr['PF']}{_(gmr['PF'])}{gmr['PTS']}{_(gmr['PTS'])}")

        for feature in total.keys():
            total[feature] += float(gmr[feature])
    print('Team Totals  ', end='   ')
    for num in total.values():
        if list(total.values()).index(num) not in (2, 5, 8):
            print(int(num), end=_(int(num)))
        else:
            print(float("{:.2f}".format(num)), end=_(float("{:.2f}".format(num))))