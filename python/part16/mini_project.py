"""Mini project: a calculator migrated from the original calculator lesson."""


def calculate(first, second, choice):
    operations = {"1": first + second, "2": first - second, "3": first * second, "7": first ** second}
    if choice in operations:
        return operations[choice]
    if choice == "4":
        return first / second if second else "Error: division by zero"
    if choice == "5":
        return first // second if second else "Error: division by zero"
    if choice == "6":
        return first % second if second else "Error: modulus by zero"
    return "Invalid choice"


def main():
    first = float(input("First number: "))
    second = float(input("Second number: "))
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    print("5. Floor division\n6. Modulus\n7. Power")
    print(calculate(first, second, input("Choice (1-7): ")))

if __name__ == "__main__":
    main()
