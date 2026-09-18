class Calculator:
    """Performs basic mathematical operations."""

    def add(self, first_number, second_number):
        """Return the sum of two numbers."""
        return first_number + second_number

    def subtract(self, first_number, second_number):
        """Return the difference of two numbers."""
        return first_number - second_number

    def multiply(self, first_number, second_number):
        """Return the product of two numbers."""
        return first_number * second_number

def main():
    """Runs calculator operations and handles user interaction."""

    calculator = Calculator()

    print("""Pick an Operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    """)
    operation = input("Enter the number for your desired operation: ")

    if operation not in ("1", "2", "3"):
        print("Selection is invalid")
        return

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    match operation:
        case "1":
            result = calculator.add(first_number, second_number)
            print(f"The sum of {first_number} + {second_number} is {result}")
        case "2":
            result = calculator.subtract(first_number, second_number)
            print(f"The difference of {first_number} - {second_number} is {result}")
        case "3":
            result = calculator.multiply(first_number, second_number)
            print(f"The product of {first_number} * {second_number} is {result}")


main()