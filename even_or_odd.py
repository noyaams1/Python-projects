while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    try:
        number = float(user_input)
        if number.is_integer():
            if int(number) % 2 == 0:
                print("Even")
            else:
                print("Odd")
        else:
            print("The number is not an integer.")
    except ValueError:
        print("That's not a valid number. Please try again.")
