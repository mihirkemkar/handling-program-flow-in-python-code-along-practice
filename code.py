# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)


 
# Code starts here
         

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
first_innings_deliveries = data['innings'][0]['1st innings']['deliveries']
count_deliveries = 0
for faced in first_innings_deliveries:
    for delivery_number, delivery_info in faced.items():
        if delivery_info['batsman'] == 'SC Ganguly':
            count_deliveries +=1
print("The deliveries faced by SC Ganguly :", count_deliveries)

#  Who was man of the match and how many runs did he scored ?
man_match = data['info']['player_of_match']
print("The Player Of The Match Is :",man_match[0])
runs_scored = 0
for runs in first_innings_deliveries:
    for delivery_number, delivery_info in runs.items():
        if delivery_info['batsman'] == 'BB McCullum':
            runs_scored += delivery_info['runs']['batsman']

print("Runs Scored By Man Of The Match Is :",runs_scored)

#  Which batsman played in the first inning?
batsman = []
for all_batsman in first_innings_deliveries:
    for delivery_number, delivery_info in all_batsman.items():
        batsman.append(delivery_info['batsman'])
print("All The Batsmen Played in First Innnings :", set(batsman))

# Which batsman had the most no. of sixes in first inning ?
most_sixes = []
for sixes in first_innings_deliveries:
    for delivery_number, delivery_info in sixes.items():
        if delivery_info['runs']['batsman'] == 6:
                most_sixes.append(delivery_info['batsman'])
print("Batsman with most sixes: ",set(most_sixes))

from collections import Counter

cnt = Counter(most_sixes)
print("The bastman who had most number of sixes : ",cnt)
def get_batsman_with_most_sixes(sixes):
    cnt = Counter(sixes)
    return cnt

#print(set(get_batsman_with_most_sixes(most_sixes)))

# Find the names of all players that got bowled out in the second innings.
second_innings_deliveries = data['innings'][1]['2nd innings']['deliveries']

bowled_players = []
for bowled_out in second_innings_deliveries:
    for delivery_number, delivery_info in bowled_out.items():
        try:
            if delivery_info['wicket']['kind'] == 'bowled':
                bowled_players.append(delivery_info['wicket']['player_out'])
        except:
            pass    


bowled_players

# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extras_1st_innings = []

for delivery_1st in first_innings_deliveries:
    for delivery_number, delivery_info in delivery_1st.items():
        if 'extras' in delivery_info:
                extras_1st_innings.append(delivery_1st)
extras_2nd_innings = []
for delivery_2nd in second_innings_deliveries:
        for delivery_number, delivery_info in delivery_2nd.items():
                if 'extras' in delivery_info:
                        extras_2nd_innings.append(delivery_2nd)


difference = len(extras_1st_innings) - len(extras_2nd_innings)
print("The extras in the second innnings were :",abs(difference))

# Code ends here


