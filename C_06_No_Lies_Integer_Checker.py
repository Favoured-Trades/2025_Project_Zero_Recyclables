# Functions go here
def int_check(question, exit_code=None):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main routine goes here

# loop
while True:
    print()

    # Ask the user their name
    name = input("Name: ")

    # Ask the user their age and check that it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is dead")
        continue
    else:
        print(f"{name} bought a ticket")
