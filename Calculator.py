def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Zero Division Error: You can't divide by zero"
    else:
        return a / b

def multiplication(a, b):
    return a * b

def main():
    while True:

        operator = input("Enter the operator to use (+, -, *, /) and q to quit: ")

        if operator.lower() == "q":
            break
        try:

            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        

        if operator == "+":
            result = add(a, b)

        elif operator == "-":
            result = subtraction(a, b)

        elif operator == "/":
            result = division(a, b)

        elif operator == "*":
            result = multiplication(a, b)
        

        else:
            result = "Invalid Operator"

        print("Result:", result)

if __name__ == "__main__":
    main()
