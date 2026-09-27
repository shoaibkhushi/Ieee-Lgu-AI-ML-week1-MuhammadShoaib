#import Random Number
import random
#rondom number function
def random_number():
    print("========Random Number Gusing Game======")
    print("1:Easy Level 1-50 With Tries 10")
    print("2:Hard Level 1-200 With Tries 5")

    while True:
        choice = input("Please Select Your Choice: ")
        if choice == "1":
            return 50,10
        elif choice == "2":
            return 200,5
        else:
            print("Invalid Choice Please Select Correct Choice Between 1 to 2.")

    
def get_guess(limit):
    while True:
        try:
            guess = int(input(f"Enter Your Guess (1-{limit}: )"))
            if guess < 1 or guess > limit:
                print(f"Please Enter A Number Between 1 and {limit}.")
                continue
            return guess
        except ValueError:
            print("Invalid Number! Please Enter A Number.")
#Play Game Function
def play_game():
    limit,tries = random_number()
    secret_number = random.randint(1,limit)
    print(f"Game Star, I am thing a number between 1 and {limit}: ")

    while tries >0:
        print(f"You have chance {tries} Left")
        guess = get_guess(limit)
        if guess == secret_number:
            print(f"Congratulation..! You Guess the right number..!")
            return
        elif guess < secret_number:
            print("Too Low...!")
        else:
            print("Too Hight...!")
        tries -= 1
    print(f"Game Finished! The Secret Number ws {secret_number}")
    print("If You Want Playing Another game Please Select (yes/no)")
    chance = input("Please Enter Your Choice: ")
    if chance == "yes".lower():
        play_game()
    elif chance == "no":
        print("Thanks")
play_game()

