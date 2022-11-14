#123 321
no = int(input("enter no"))
temp = no

#985
rem = 1
revno =0
#985 != 0 True
#98 != 0 True
#9 != 0 True
#0 != 0 False
while no!=0:
    # rem = 985 % 10 = rem =5
    #rem = 98 % 10 = rem = 8
    #rem = 9 % 10 = rem = 9
    rem = no % 10 
    #0 = 0 *10 5 = 5
    #5 = 5 * 10 + 8 = 58
    # 58 * 10 + 9 = 589
    revno = revno * 10 +rem
    #985 = 985 // 10 = 98
    #98 = 98 // 10 = 9
    #9 = 9 // 10 = 0
    no = no//10 #12
    
    
if temp == revno:
    print("no is palindrome")
else:
    print("no is not palindrome")    
    