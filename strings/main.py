# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_one = 'Ruud Gullit '
player_two = 'Marco van Basten '

goal_0 = 32
goal_1 = 54

x = 3

scorers = f'{player_one}{str(goal_0)}, {player_two}{str(goal_1)}'
print(scorers)

report = f'{player_one}scored in the {goal_0}nd minute' + f'\n{player_two}scored in the {goal_1}th minute'

print(report)

player = 'Igor Belanov'

first_name = player[:(player.find(' '))]

last_name_len = len(player)-player.find(' ')-1

name_short = player[0] + '.' + player[(player.find(' ')):]

chant = ((first_name + '! ')*(len(first_name)-1))+(first_name + '!')

good_chant_2 = bool(chant[-1] != ' ')
