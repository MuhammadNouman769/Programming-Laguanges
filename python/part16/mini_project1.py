print("=== Simple Calculator ===")
num1 = float(input("Pehla number enter karein: "))
num2 = float(input("Dusra number enter karein: "))

print("\nOperations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Modulus")
print("7. Power")

choice = input("\nApna choice (1-7) enter karein: ")

if choice == "1":
    print(f"Result: {num1 + num2}")
elif choice == "2":
    print(f"Result: {num1 - num2}")
elif choice == "3":
    print(f"Result: {num1 * num2}")
elif choice == "4":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero nahi ho sakti!")
elif choice == "5":
    if num2 != 0:
        print(f"Result: {num1 // num2}")
    else:
        print("Error: Division by zero nahi ho sakti!")
elif choice == "6":
    if num2 != 0:
        print(f"Result: {num1 % num2}")
    else:
        print("Error: Modulus by zero nahi ho sakti!")
elif choice == "7":
    print(f"Result: {num1 ** num2}")
else:
    print("Invalid choice!")