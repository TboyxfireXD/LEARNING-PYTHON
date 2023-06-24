#list comprehension offers a shorter syntax when you want to create a new list

fruitbucket = ["apple", "banana", "cherry", "kiwi", "mango"]
newbucket = []

for x in fruitbucket:
    if "a" in x:
        newbucket.append(x)
i=0
while i < (1):
    print(newbucket)
    i = i+1

#1 change all the items in the list to capital letter
fruitbucket = ["apple", "banana", "cherry", "kiwi", "mango"]
newbucket = [x.upper() for x in fruitbucket]
print(newbucket)

#2 set all items in the fruit bucket to hello
fruitbucket = ["apple", "banana", "cherry", "kiwi", "mango"]
newbucket = []

for x in fruitbucket:
    if x != "hello":
     newbucket.append("hello")
    print(newbucket[0])

#3 return orange instead of banana
fruitbucket = ["apple", "banana", "cherry", "kiwi", "mango"]
newbucket = [x for x in fruitbucket if x != "banana"] ;
newbucket.insert(1, "orange")
print(newbucket)


def reverse (g):
    str = ""
    for h in g:
        str = h + str
    return str
g = "Dansol Schools" 
print(reverse(g)) 

