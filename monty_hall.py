import random
door = [1,2,3]
total = 0
win = 0
win_n=0

for i in range(1,10000000):

    door_list = door[:]
    final_choice = door[:]
    choice = random.randint(1,3)
    correct = random.randint(1,3)
    if choice == correct:
        win_n = win_n +1
    #print(door_list)
    #print(choice)
    #print(correct)
    door_list.remove(choice)
    for item in door_list:
        if item == correct:
            door_list.remove(correct)
    a = random.randint(0,len(door_list)-1)
    door_removed = door_list.pop(a)
    #print(door_removed)
    #print(final_choice)
    final_choice.remove(door_removed)
    final_choice.remove(choice)
    final_choice= final_choice.pop(0)
    if final_choice == correct:
        win = win+1
    total = total+1
print("Total: ",total )
print("Win Not Switching: ",win_n  )
print("Win Switching: ", win )


percentage = (win/total)*100
print("Win Rate switching: ",percentage,"%")
percentage = (win_n/total)*100
print("Win Rate not switching: ",percentage,"%")