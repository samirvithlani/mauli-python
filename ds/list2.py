weeklySales = [[100,200,300],[450,452,456],[789,789,789],[123,123,123],[456,456,456],[785,96,52],[123,785,965]]

#dailySales = 0

for i in range(0,len(weeklySales)):
    dailySales=0
    print("day ",i+1,end=" ")
    for j in range(0,len(weeklySales[i])):
        print(weeklySales[i][j])
        dailySales = dailySales + weeklySales[i][j]
        
    print("Total sales for the day is",dailySales)    