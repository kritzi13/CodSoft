def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operator():
    operators = ['+', '-', '*', '/']
    while True:
        op = input("Choose operation (+, -, *, /): ")
        if op in operators:
            return op
        else:
            print("Invalid operator. Please choose from +, -, *, /.")

def calculator():
    print("Welcome!")
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operator = get_operator()

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)

        print(f"Result: {result}")

        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("Goodbye!")
            break

calculator()
