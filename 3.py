airport_data = {}
def enter_new_airport():
    code = input("Enter the airport code: ")
    name = input("Enter the airport name: ")
    airport_data[code] = name
    print("Airport data entered successfully!")

def fetch_airport_info():
    code = input("Enter the airport code: ")
    if code in airport_data:
        print("Airport Name:", airport_data[code])
    else:
        print("Airport data not found!")

while True:
    print("Choose an option:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enter_new_airport()
    elif choice == "2":
        fetch_airport_info()
    elif choice == "3":
        print("Program execution ended.")
        break
    else:
        print("Invalid option! Please choose a valid option.")
