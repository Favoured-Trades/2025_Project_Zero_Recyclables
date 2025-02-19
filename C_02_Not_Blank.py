def not_blank(question):
    """Checks that a user response is not blank"""

    # Repeats until return
    while True:
        response = input(question).strip()

        if response != "":
            return response

        print("Sorry, this can't be blank. Please enter something.\n")


# Main routine starts here
who = not_blank("Please enter your name: ")
print(f"Hello {who}")
