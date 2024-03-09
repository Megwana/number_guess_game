import random

def guess_number(): 
    while True:
        top_of_range_input = input("Type a number: ").strip()
        if top_of_range_input.isdigit():
            top_of_range = int(top_of_range_input)
            if top_of_range <= 0:
                print("You must provide a random number larger than 0.")
            else:
                break
        else:
            print("Please enter a valid number.")

    random_number = random.randint(0, top_of_range)

    while True:
        user_guess = input("Make a guess: ").strip()
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please enter a valid number.")
            continue

        if user_guess == random_number:
            print("Well done, that's correct!")
        else: 
            print(f"Sorry, you got it wrong, it was {random_number}")
            quit()

guess_number()
