# nested loop = a loop withing another loop(outer,inner)
# outer loop:
#     inner loop:
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="") #TO BE IN THE SAME ROW
    print()