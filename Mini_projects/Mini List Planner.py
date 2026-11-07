print("MY AUTUMN BREAK PLANNER🏷")
n=int(input("How many activities you want to do ? "))
act= []
for i in range(n):
    act_n=input("Enter name of the Activity :")
    act.append(act_n)
print("Activities are :", act)
print("Total activities :", len(act))
fav= input("Enter your favourite activity: ")
if fav.lower() in [a.lower() for a in act]:
    print("Yay!!😸", fav,
          "is in your planner list.")
else:
    print(fav, "is not in your planner list.")
print("REVERSED ACTIVITY LIST:")
print(act[::-1])
name = input("Enter your name: ")
print("Keep creating and learning and have a great Autumn break😄,", name + "!")
print("Never Stop learning!☺️")
