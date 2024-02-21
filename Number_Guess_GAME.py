import random
target = random.randint(1,100)
while True:
    user_input = (input("Enter a number to guess OR 'Q' to QUIT\n")).lower()
    if user_input == 'q':
        break
    user_input = int(user_input)
    if (user_input == target):
        print("Congratulations You guess the Correct Number")
        break
    elif (user_input < target):
        print("Your guess was too low, take a Bigger umber")
    else:
        print("Your guess was too high, take a smaller number")
print("-----GAME OVER------\n" "Thanks for playing")