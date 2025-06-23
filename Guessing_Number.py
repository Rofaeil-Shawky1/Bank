import random

secret_number = random.randint(1, 10)

tries = 0

while True:
    guess = int(input(" Enter A Number"))
    tries += 1

    if guess < secret_number:
        print("Greatest than number ")
    elif guess > secret_number:
        print("Smaller tn number")
    else:
        print("Congratulations , you are Winning after : ", tries )
        break
6