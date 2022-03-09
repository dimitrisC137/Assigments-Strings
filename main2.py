player = "Marco van Basten"
first_name = player[0:5] #I dont know how to use slicing and the find-method to isolate and store the first letter, can you please show me?
last_name =  player[6:] 
last_name_len = len(last_name)
dot = ". "
name_short = first_name[0] + dot + last_name
chant = f" {first_name}!"
print ((chant)*len(first_name))