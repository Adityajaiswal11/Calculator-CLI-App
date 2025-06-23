import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("=== CLI Calculator ===")
    print("Select an operation:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Exit")

def get_numbers():
    raw = input("Enter numbers separated by space: ")
    try:
        numbers = [float(num) for num in raw.strip().split()]
        if len(numbers) < 2:
            print("Please enter at least two numbers.")
            return None
        return numbers
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None

def calculate(choice, numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if choice == '1':
            result += num
        elif choice == '2':
            result -= num
        elif choice == '3':
            result *= num
        elif choice == '4':
            if num == 0:
                print("Error: Division by zero.")
                return None
            result /= num
    return result

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Press Enter to try again.")
            input()
            continue

        numbers = get_numbers()
        if numbers is None:
            input("Press Enter to continue...")
            continue

        result = calculate(choice, numbers)
        if result is not None:
            print(f"Result: {result}")

        input("Press Enter to continue...")

# Run the app
if __name__ == "__main__":
    main()
