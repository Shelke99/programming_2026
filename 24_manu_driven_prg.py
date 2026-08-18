# 26. Build a menu-driven program (repeat options until quit).
def main_menu():
    print("\n ---------------Menu-----------------")
    print("1. Add two numbers ")
    print("2. Subtract two numbers ")
    print("3. Quit ")

def get_num():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2
    
def run_program():
    main_menu()
    while True:

        choice = input("Enter your choice(1-3): ")

        if choice == '1':

            n1,n2 = get_num()
            print(f"results: {n1 + n2}")

        elif choice == '2':

            a,b = get_num()
            print(f"Result: {a - b}")

        elif choice == '3':
            print("Exiting Program..........Goodbye!")
            break

        else:
            print("Please enter the correct number in range within 1-3...")
run_program()