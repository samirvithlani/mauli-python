sales =[145,25,123,699,78,85,50,699]
#145
max = sales[0]

#
'''
for i in sales:
    # 145 > 145 false max = 145
    # 25 > 145 false max = 145
    #123 > 145 false max = 145
    #699 > 145 true max = 699
    #78 > 699 false max = 699
    #85 > 699 false max = 699
    #50 > 699 false max = 699
    if i > max:
        #max = 699
        
        max = i
'''



#0
for i in range(0,len(sales)):
    #sales[0] = 145 > 145 false max = 145
    #sales[1] = 25 > 145 false max = 145
    #sales[2] = 123 > 145 false max = 145
    #sales[3] = 699 > 145 true max = 699
    if sales[i] > max:
        max = sales[i]
        index = i
        
print("Max sales is",max)
print("Index is",index+1)