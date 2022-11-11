age = int(input("enter age"))


if age>=18:
    print("you are eligible to vote")
    if age>=21:
        print("you are eligible for marriage")
    else:
        print("you are not eligible for marriage")
        
else:
    print("you are not eligible to vote")
    if age>=5:
        print("you are eligible for school")
    else:
        print("you are not eligible for school")            