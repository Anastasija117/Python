# collection = single "variable" used to store multiple vlues
#  Lists = [] ordered and changeable.Duplicates OK
#  Set   = {} unordered and immutable, but Add/Remove OK.NO duplicates
#  Tuple = () ordered and unchangeable.Duplicates OK.FASTER

fruits = ("apple","pear","orange","coconut","coconut")
#print(dir(fruits))
#print(help(fruits))
#print(fruits[::-1])
#for fruit in fruits:
#    print(fruit)
#print(len(fruits))
#print("pineapple" in fruits)

#fruits[1] = "pinapple"
#fruits.append("pineapple") #TO ADD
#fruits.remove("apple") to remove
#fruits.insert(0,"pineapple") to add to a place
#fruits.sort() aplhabetic order
#fruits.reverse() reversed order not alhabetical
#fruits.clear() all elements are gone
# print(fruits.index("coconut")) on what spot is it
#print(fruits.count("apple"))


#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()


#print(fruits.index("apple"))
#print(fruits.count("coconut"))
for fruit in fruits:
    print(fruit)
