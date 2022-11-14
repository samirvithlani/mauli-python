no = int(input("enter no"))

#123 1 + 2 +3  = 6
#123 1 * 2 * 3 = 6
rem =0
sum =0
mul =1
while no!=0:
    rem = no % 10 # 3 2 1
    
    sum = sum + rem
    #0 = 0 + 3 = 3
    #3 = 3 + 2 = 5
    #5 = 5 + 1 = 6
    mul = mul * rem
    no = no//10
    #123 //10 12
    #12 // 10 = 1
    #1 // 10 = 0
    
if sum == mul:
    print("no is twin")
    
else:
    print("no is not twin")    