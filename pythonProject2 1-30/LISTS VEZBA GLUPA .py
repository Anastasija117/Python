names = []
myself = []
girlfriend = []
besties = []
besties_pos = []
besties_pos_int = []
sis = []
mom = []
while True:
    name = input("Enter a name for a list(q to quit): ")
    if name.lower() == "q":
        break
    else:
        names.append(name)
print("You have entered the following names: ")
for name in names:
    print(name, end=" ")
print()
my_name = int(input("In what position is your name? "))
myself.append(names[my_name])
for n in myself:
    print(f"Your name is {myself}.")
print()
my_sis = int(input("In what position is your sister's name? "))
sis.append(names[my_sis])
for n in sis:
    print(f"Your sister's name is {sis}.")
print()
my_mom = int(input("In what position is your mother's name? "))
mom.append(names[my_mom])
for n in mom:
    print(f"Your mom's name is {mom}.")
print()
my_gf = int(input("In what position is your girlfriend's name? "))
girlfriend.append(names[my_gf])
for n in girlfriend:
    print(f"Your girlfriend's name is {girlfriend}.")
print()
my_bff = int(input("How many bffs have you entered?: "))
for n in range(0, my_bff):
    besties_pos.append(input("Enter their positions: "))
for i in besties_pos:
    besties_pos_int.append(int(i))
for pos in besties_pos_int:
    if pos < len(names):
        besties.append(names[pos])
print("Your best friends are")
print(besties,end=" ")
input("The end")