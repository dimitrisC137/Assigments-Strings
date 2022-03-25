
player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = player_0 + " " + str(goal_0) + ", " + player_1 + " " + str(goal_1)
report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute"  
print(scorers)

player = "Marco van Basten"
first_name = player[:player.find(" ")]
last_name = player [player.find(" ")+1:]
last_name_len = len(last_name)
name_short = first_name[0] + ". " + last_name
chant = (first_name + "!" + " ") * (len(first_name)-1) + first_name + "!"
good_chant = chant[-1] != " "
print(good_chant) 


