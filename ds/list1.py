#index index always starts from 0

weeklySales =[1256, 2345, 3456, 4567, 5678, 6789, 7890]
totalSales=0
'''
for i in range(0,7):
    print("Day",i +1,"sales",weeklySales[i])
    #0 = 0 + 1256 = 1256
    #1256 = 1256 + 2345 = 3601
    totalSales = totalSales + weeklySales[i]

print("Total sales for the week is",totalSales)    
'''

for i in weeklySales:
    print(i)

'''
print(weeklySales[0])
print(weeklySales[1])
print(weeklySales[2])
print(weeklySales[3])
print(weeklySales[4])
print(weeklySales[5])
print(weeklySales[6])
'''