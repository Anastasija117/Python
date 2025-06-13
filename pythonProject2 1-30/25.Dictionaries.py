# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates
from dis import CACHE

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("Japan"))

#if capitals.get("Russia"): TO CHECK IF ITS IN THE COLLECTION
#    print("That capital exists")
#else:
#    print("That capital doesn't exist")

#capitals.update({"Germany":"Berlin"}) ADD
#capitals.update({"USA":"Detroit"}) UPDATE

#capitals.pop("China") REMOVE

#capitals.popitem() REMOVE LATEST KEY VALUE PAIR

# capitals.clear() REMOVE ALL

#keys = capitals.keys()  TO GET THE 1ST WORD(THE KEYS)

#for key in capitals.keys():
#    print(key)

#values = capitals.values() TO GET THE 2ND WORD(THE VALUES)

#for value in capitals.values():
#    print(value)

#items = capitals.items()
#for key,value in capitals.items():
#    print(f"{key}:{value}")