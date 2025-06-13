print("This is a program that calculates the sum of all even numbers between 1 and the number we input!")
number = int(input("Enter the number you want to calculate to: "))
sum = 0
even_num = 0
for x in range(1, number):
    if x % 2 == 0:
        print(f"Even number {x} is being added to the sum: {sum}")
        sum = sum + x
        even_num += 1
if number % 2 == 0:
    even_num += 1
    sum = sum + number
print(f"There are {even_num} even numbers between 1 and {number}.The sum of those is : {sum}")

input("The end")
