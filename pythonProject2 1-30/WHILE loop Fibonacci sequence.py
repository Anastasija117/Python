
n = int(input("Enter a number that determines how many numbers \n"
              "of the Fibonacci squence to generate: "))
s = 0
a = int(input("What is the first number?: "))
b = int(input("What is the second number?: "))
while s < n:
    print(a)
    a,b = b, a+b
    s += 1
input("\n\n\nThe end")