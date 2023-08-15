import random

userinp_odd_even = input("Odd or Even: ")
if userinp_odd_even.capitalize() == "Odd":
    user_choose_odd = True
elif userinp_odd_even.capitalize() == "Even":
    user_choose_odd = False
else:
    print("Enter only either 'Odd' or 'Even' not anything else")
    exit()

user_input1 = int(input("Enter a number in the range of [0,6]: "))
if user_input1 > 6:
    print("Choose a number only between 0 and 6 including 0,6 not more or less than that")
    exit()
comp_input1 = random.randrange(7)
bool1 = True
while bool1:
    toss_sum = user_input1 + comp_input1
    if toss_sum % 2 == 0 or toss_sum == 0:
        is_odd = False
    else:
        is_odd = True

    if user_choose_odd == is_odd:
        user_win_toss = True
        print(f"The sum is {toss_sum}, You win the toss")
    else:
        user_win_toss = False
        print(comp_input1)
        print(f"The sum is {toss_sum}, You lost the toss")
    bool1 = False
computers_turn = False
user_score1 = 0
computer_score1 = 0
if user_win_toss == True:
    user_input2 = input("Choose to bat or bowl: ")
    if user_input2.capitalize() == "Bat":
        bool2 = True
        while bool2:
            comp_input2 = random.randrange(7)
            user_input2 = int(input("Enter a number in the range [0,6]: "))
            if user_input2 > 6:
                print("Choose a number only between 0 and 6 including 0,6 not more or less than that")
                exit()
            if comp_input2 == user_input2:
                print("You are out")
                print(f"The computer choose {comp_input2} and your runs are {user_score1}")
                print("It's your turn to bowl now, enter the same as the computer to take the wicket ")
                bool2 = False
                computers_turn = True
            else:
                user_score1 = user_score1 + user_input2
                print(f"The computer choose {comp_input2} and your runs are {user_score1}")
        while computers_turn:
            if computer_score1 > user_score1:
                print(f"You lost the game, Your score {user_score1}, computer score {computer_score1}")
                exit()
            comp_input3 = random.randrange(7)
            user_input3 = int(input("Enter a number in the range [0,6]: "))
            if user_input3 > 6:
                print("Choose a number only between 0 and 6 including 0,6 not more or less than that")
                exit()
            if comp_input3 == user_input3:
                print("The computer is out")
                print(f"The computer choose {comp_input3} and it's runs are {computer_score1}")
                computers_turn = False
            else:
                computer_score1 = computer_score1 + comp_input3
                print(f"The computer choose {comp_input3} and it's runs are {computer_score1}")
        if user_score1 > computer_score1:
            print(f"Your score is {user_score1} and computer score is {computer_score1}")
            print(f"You win by {user_score1 - computer_score1} runs")
        else:
            print(f"Your score is {user_score1} and computer score is {computer_score1}")
            print(f"You lost the game")
    elif user_input2.capitalize() == "Bowl":
        computers_turn = True
        user_turn = False
        while computers_turn:
            comp_input3 = random.randrange(7)
            user_input3 = int(input("Enter a number in the range [0,6]: "))
            if user_input3 > 6:
                print("Choose a number only between 0 and 6 including 0,6 not more or less than that")
                exit()
            if comp_input3 == user_input3:
                print("The computer is out")
                print(f"The computer choose {comp_input3} and it's runs are {computer_score1}")
                print("Its your turn to bat now, score higher than the computer to win")
                computers_turn = False
                user_turn = True
            else:
                computer_score1 = computer_score1 + comp_input3
                print(f"The computer choose {comp_input3} and it's runs are {computer_score1}")
        while user_turn:
            if user_score1 > computer_score1:
                print(f"You won the game, Your score {user_score1}, computer score {computer_score1}")
                exit()
            comp_input2 = random.randrange(7)
            user_input2 = int(input("Enter a number in the range [0,6]: "))
            if user_input2 > 6:
                print("Choose a number only between 0 and 6 including 0,6 not more or less than that")
                exit()
            if comp_input2 == user_input2:
                print("You are out")
                print(f"The computer choose {comp_input2} and your runs are {user_score1}")
                user_turn = False
                computers_turn = True
            else:
                user_score1 = user_score1 + user_input2
                print(f"The computer choose {comp_input2} and your runs are {user_score1}")
    else:
        print("Choose either Bat or Bowl not anything else")
elif user_win_toss == False:
    choices = ["Bat", "Bowl"]
    computer_choice = random.choice(choices)
    if computer_choice == "Bat":
        print("Computer choose to Bat first")
        computers_turn = True
        user_turn = False
        while computers_turn:
            comp_input3 = random.randrange(7)
            user_input3 = int(input("Enter a number in the range [0,6]"))
            if user_input3 > 6:
                print("Choose a number only between 0 and 6 including 0,6 not more or less than that")
                exit()
            if comp_input3 == user_input3:
                print("The computer is out")
                print(f"The computer choose {comp_input3} and it's runs are {computer_score1}")
                print("Its your turn to bat now, score higher than the computer to win")
                computers_turn = False
                user_turn = True
            else:
                computer_score1 = computer_score1 + comp_input3
                print(f"The computer choose {comp_input3} and it's runs are {computer_score1}")
        while user_turn:
            if user_score1 > computer_score1:
                print(f"You won the game, Your score {user_score1}, computer score {computer_score1}")
                exit()

            comp_input2 = random.randrange(7)
            user_input2 = int(input("Enter a number in the range [0,6]"))
            if user_input2 > 6:
                print("Choose a number only between 0 and 6 including 0,6 not more or less than that")
                exit()
            if comp_input2 == user_input2:
                print("You are out")
                print(f"The computer choose {comp_input2} and your runs are {user_score1}")
                user_turn = False
            else:
                user_score1 = user_score1 + user_input2
                print(f"The computer choose {comp_input2} and your runs are {user_score1}")
        if computer_score1 > user_score1:
            print(f"You lost the game, Your score {user_score1}, computer score {computer_score1}")
            exit()
    elif computer_choice == "Bowl":
        print("The computer choose to Bowl first")
        bool2 = True
        while bool2:
            comp_input2 = random.randrange(7)
            user_input2 = int(input("Enter a number in the range [0,6]: "))
            if user_input2 > 6:
                print("Choose a number only between 0 and 6 including 0,6 not more or less than that")
                exit()
            if comp_input2 == user_input2:
                print("You are out")
                print(f"The computer choose {comp_input2} and your runs are {user_score1}")
                print("It's your turn to bowl now, enter the same as the computer to take the wicket ")
                bool2 = False
                computers_turn = True
            else:
                user_score1 = user_score1 + user_input2
                print(f"The computer choose {comp_input2} and your runs are {user_score1}")
        while computers_turn:
            if computer_score1 > user_score1:
                print(f"You lost the game, Your score {user_score1}, computer score {computer_score1}")
                exit()
            comp_input3 = random.randrange(7)
            user_input3 = int(input("Enter a number in the range [0,6]: "))
            if user_input3 > 6:
                print("Choose a number only between 0 and 6 including 0,6 not more or less than that")
                exit()
            if comp_input3 == user_input3:
                print("The computer is out")
                print(f"The computer choose {comp_input3} and it's runs are {computer_score1}")
                computers_turn = False
            else:
                if computer_score1 > user_score1:
                    break
                else:
                    computer_score1 = computer_score1 + comp_input3
                    print(f"The computer choose {comp_input3} and it's runs are {computer_score1}")
        if user_score1 > computer_score1:
            print(f"Your score is {user_score1} and computer score is {computer_score1}")
            print(f"You win by {user_score1 - computer_score1} runs")















