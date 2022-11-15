users = {1:["raj","ram","riya"],2:["jay","jaya","jap"],3:("priyanka","parth","prit")}


users[3] = ("priyanka","n")

for i in users:
    print(i)
    for x in users[i]:
        print(x)
    print("\n")    