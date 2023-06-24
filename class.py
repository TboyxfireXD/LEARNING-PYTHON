mylist = ["car", "house", "food", "job"]
print(len(mylist))

mylist[0] = ("benz", "ferarri", "toyota", "lamborghini")
mylist[1] = ("flat", "appartment", "bungalow", "skyscraper")
mylist[2] = ("garri", "groundnut", "eba", "amala")
mylist[3] = ("doctor", "engineer", "lawyer", "nurse")
print(mylist[3])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
thislist[0] = "blackcurrant"
thislist[1] = "watermelon"
print(thislist)

thisfruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
print(thisfruit[2:5])

list = ["apple", "banana", "cherry"]
list.append("orange")
list.insert(1, "mango")
list.clear()
print(list)


#while loop - the while loop function determines the length of the list, 
# then start at 0 and loop your way through the list items by referring to their indexes

thelist = ["Promise", "Tosin", "Jude", "Toni"]
i = 0
while i >len(thelist):
    print(thelist[i])
    i = i+1

#.pop() removes a value(or constant) from the back and you could also specify the index you want to remove
#.append() the append command adds items to the end of the list
#.insert() adds value to a given position
#.remove() removes values using name

#use the following loop methods to loop through the itemlist
# 1. loop through list method
# 2. loop through the index number
# 3. while loop
itemlist = ["Church", "Mosque", "Gym", "Bar", "Carwash"]

fruitbucket = ["apple", "banana", "cherry", "kiwi", "mango"]
newbucket = []

#iterating through the fruitbucket without if
fruitbucket = ["apple", "banana", "cherry", "kiwi", "mango"]
newbucket = [x for x in fruitbucket]
print(newbucket)

#iterating through objectslike a tuple, list, set, etc
numberlist = [x for x in range (10)]
newlistnum = [x for x in numberlist if x!= 7]
print(newlistnum)

#create a variable list that accepts only numbers lower than 5

classnumli = [x for x in range (10)]
classnumlinew = [x for x in classnumli if x < 5]
print(classnumlinew)

fruitbucket = ["orange", "mango", "kiwi", "pineapple", "banana", "cherry"]
fruitbucket.sort()
print(fruitbucket)

Thislist = ["orange", "mango", "kiwi", "pineapple", "banana", "cherry"]
Thislist.reverse()
print(Thislist)

salary = 900
salary += 200
print (salary)

fruitbucket = ["apple ", "banana ", "cherry ", "kiwi ", "mango "] 