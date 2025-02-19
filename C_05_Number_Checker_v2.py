# Functions go here
def num_check(question, low, high, exit_code):
    """Checks users enter an integer between two values"""

    error = f"Oops - please enter an integer between {low} and {high}"

    while True:
        response = input(question).lower()

        # Check for exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(response)

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

# loop
while True:
    print()

    my_num = num_check("Pick a number between 1 and 10: ", 1, 10, "xxx")

    if my_num == "xxx":
        print("You chose to exit")
    else:
        print(f"You chose {my_num}")