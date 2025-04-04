def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b if b != 0 else "Error! Division by zero."


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter the operation (1/2/3/4): ")

    choices = ["1", "2", "3", "4"]
    if choice in choices:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")

        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
if __name__=="__main__":
    calculator()