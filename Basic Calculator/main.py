# define the functions needed, add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")

def div(a,b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n" )
while True:
    print("A. addition")
    print("B. subtraction")
    print("C. division")
    print("D. multiplication")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a,b)
    elif choice == "b" or choice =="B":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a, b)
    elif choice == "c" or choice =="C":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mul(a, b)
    elif choice == "d" or choice =="D":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()


