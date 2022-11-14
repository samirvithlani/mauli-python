#370 370 153 
#1 ** 5 ** 3 **
#1 + 125 + 27 = 153
no = int(input("enter no"))
temp = no

rem =0
digit =0
#153
#15
#1
while no!=0:
    #3 5
    rem = no%10
    #0 = 0  + 27 = 27
    #27 = 27 + 5 ** 3 = 152
    #152 = 152 + 1 ** 3 = 153
    
    digit = digit + rem **3
    no = no//10
    #153 //10 15
    #1
    
if temp ==digit:
    print("no is armstrong")
else:
    print("no is not armstrong")        
