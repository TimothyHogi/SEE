import random
print("Welcome to the Number guessing game")
secret_number = random.randint(1, 50)
for attempt in range(1,6):
    guess = int(input(f"Attempt {attempt}/5 - Guess a number between 1 and 50: "))
    if guess < secret_number:
        print ("Too Low!")
    elif guess > secret_number:
        print ("Too high!")
    else:
            print(f"correct! The number was {secret_number}. You got it in {attempt} tries!")
            break
else:
    print(f"Sorry! The number was {secret_number}. Better luck next time!")

