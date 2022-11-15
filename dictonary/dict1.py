#key value pair index index [0]
# 200 week 
# dates : salesvalue

data = {"14-02-2022":20,"19-02-2022":90,"1-04-2022":250,"28-02-2022":200,"18-03-2022":50,"14-02-2022":450}
print(data["14-02-2022"])
#get will return value
sp = data.get("14-02-2022")
print(sp)

removedvalue = data.pop("1-04-2022")
print(removedvalue)

key = data.keys()
print(key)




x = data.popitem()
print(x)



for i in data:
    print(i," = ",data[i])
