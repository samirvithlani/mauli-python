#multipule conditions

#> 25 even
#and op and or op#
#no >20 and no %2 ==0
#and
'''
    t    t    t
    f   -    f
    t    f   f
'''
#or
'''
    t   -   t
    f   t   t
    f   f   f
       
'''
no = int(input("enter no"))
if no >20 or no %2 ==0:
    print("true")
else:
    print("false")    