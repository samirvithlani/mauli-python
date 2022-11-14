'''
    i=1 initial value
    i<=10 condition
    i++ increment
    for(i=1;i<=10;i++){
        print(i)
    }
    i =1
    1<=10 TRue
    1
    i = i +1 =2
    i =2
    2<=10 TRue
    2
    i =2
    3<=10 TRue
    3
    i =10
    10<=10 TRue
    10
    i =11
    11<=10 false
    

'''
sum=0
for i in range(1,6):
    #0 = 0 + 1 sum =1
    #1 = 1 + 2 sum =3
    #3 = 3 + 3 sum =6
    #6 = 6 + 4 sum =10
    #10 = 10 + 5 sum =15
    sum = sum +i
    print(i)

print("sum of 1 to 5 is",sum)    