from pathlib import Path

def add(a, b) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b) -> float:
    return a - b


def multiply(a, b) -> float:
    return a * b


def divide(a, b) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_number(prompt: str) -> float:
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    while True:
        print("\nChoose an operation:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  q. Quit")

        choice = input("Your choice: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice, please try again.")
            continue

        name, func = operations[choice]
        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")

        try:
            print(f"{name} result: {func(a, b)}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()