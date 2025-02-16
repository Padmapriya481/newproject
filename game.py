import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)  # Generate a random number
    tries = 0
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess = input("Take a guess (or type 'quit' to exit): ")
        
        if user_guess.lower() == "quit":
            print("Okay, the number was {}.".format(number_to_guess))
            break
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("That's not a valid number.")
            continue
        
        tries += 1
        
        if user_guess == number_to_guess:
            print("Congratulations, you found the number in {} tries.".format(tries))
            break
        elif user_guess < number_to_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

if __name__ == "__main__":
    number_guessing_game()
