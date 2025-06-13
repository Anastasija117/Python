n = int(input("How many numbers are in your list?: "))
numbers = []
for x in range(n):
    number = int(input("Enter a number: "))
    numbers.append(number)
print(f"Your list is: {numbers}")
print()
sum = 0
even_numbers = []
odd_numbers = []
multiplied = []
reversed = []
for number in numbers:
    sum = sum + number
    if number % 2 == 0:
        even_numbers.append(number)
    elif number % 2 == 1:
        odd_numbers.append(number)
    multiplied.append(number * 2)
    max_num = max(numbers)
    min_num = min(numbers)
    reversed = numbers[::-1]
print(f"1.Sum of numbers: {sum}")
print(f"2.Even numbers: {even_numbers}")
print(f"3.Odd numbers: {odd_numbers}")
print(f"4.Multiply each by 2: {multiplied}")
print(f"5.Max and min: {max_num},{min_num}")
print(f"6.Reversed list: {reversed}")
input("The end")