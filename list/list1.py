#array always starts with 0
students = ["raj","jay","parth","priya","amit","sachin","sachin"]

students.append("ram") #add element at the end of the list
students.extend(["shyam","mohan"]) #add multiple elements at the end of the list
#students.pop() #remove last element from the list
#students.remove("sachin") #remove element from the list
#students.clear() #remove all elements from the list
#students.sort() #sort the list
print(students.count("sachina"))
#overloding 
students.insert(0,"raja") #insert element at specific position
removedelement = students.pop(1) #remove element from specific position
print("removing....",removedelement)

for i in students:
    print(i)
    
#for i in range(0,len(students)):
    #print(students[i])