def check_even_odd(number):
    """
    Determines if an integer is even or odd using the modulus operator.
    """
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"


def main():
    try:
        # Prompt the user to enter an integer
        user_input = int(input("Enter an integer: "))
        result = check_even_odd(user_input)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
    