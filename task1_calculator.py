"""Task 1: Simple CLI Calculator"""


def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return "Error: division by zero" if b == 0 else a / b
    return "Error: invalid operator"


def main():
    print("=== Simple Calculator ===")
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ").strip()
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.\n")
            continue
        print(f"Result: {calculate(a, b, op)}\n")
        if input("Another calculation? (y/n): ").strip().lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
