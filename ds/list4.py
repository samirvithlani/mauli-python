sales =[145,25,123,699,78,85,50,699]
no = int(input("Enter a number: "))
index =0

flag =0
for i in range(0,len(sales)):
    if sales[i] ==no:
        index = i
        flag=1
        break
        
        

if(flag==1):
    print("Found",index+1)
else:
    print("Not found")        
    
    