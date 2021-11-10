import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99", end="")
print("to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck\n")

found = 0
count = 0
correct_nb = random.randint(1, 99)
while found == 0:
    choice = input("What's your guess between 1 and 99?\n>> ")
    count = count + 1
    if choice == "exit":
        print("Goodbye!")
        found = -1
    elif len(choice) > 0 and choice[0] == '-' and choice[1:].isdigit():
        print("Not a positive number..")
    elif not choice.isdigit():
        print("That's not even a number..")
    elif int(choice) < correct_nb:
        print("Too low!")
    elif int(choice) > correct_nb:
        print("Too high!")
    elif int(choice) == correct_nb:
        print("Congratulations, you've got it!")
        print(f"You won in {count} attempts!")
        found = 1
    if count == 1 and found == 1:
        if correct_nb == 42:
            print("The answer to the ultimate question of life,", end="")
            print("the universe and everything is 42.")
        print("Congratulations! You got it on your first try!")
