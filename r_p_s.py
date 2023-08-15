import random

user_score = 0
comp_score = 0
comp_options = ['Rock', 'Paper', 'Scissors']

def taking_input():
    global user_input, comp_input
    user_input = input("Rock, Paper or Scissors? ").capitalize()
    comp_input = random.choice(comp_options)

def user_win():
    global user_score
    user_score += 1
    print(f"Computer choose {comp_input}")
    print(f"You won this round "
          f"Your Score: {user_score}, Computer Score: {comp_score}")


def comp_win():
    global comp_score
    comp_score += 1
    print(f"Computer choose {comp_input}")
    print(f"Computer won this round "
          f"Your Score: {user_score}, Computer Score: {comp_score}")


def user_loose():
    global comp_score
    comp_score += 1
    print(f"Computer choose {comp_input}")
    print(f"Computer won this round"
          f"Your Score: {user_score}, Computer Score: {comp_score}")

def comp_loose():
    global user_score
    user_score += 1
    print(f"Computer choose {comp_input}")
    print(f"You won this round"
          f"Your Score: {user_score}, Computer Score: {comp_score}")

def tie():
    print(f"Computer choose {comp_input}")
    print(f"Its a tie for this round since you both choose the same")


def game_end():
    if comp_score > user_score:
        print("Computer won this game")
        print(f"Computer score: {comp_score}"
              f"Your score: {user_score} ")
    else:
        print("You won this game!")
        print(f"Your score: {user_score} \n"
              f"Computer score: {comp_score} ")

while True:
    try:
        if comp_score >= 3 or user_score >= 3:
            game_end()
            break
        taking_input()
        if comp_input == 'Rock' and user_input == 'Rock':
            tie()
        elif comp_input == 'Rock' and user_input == 'Paper':
            user_win()
        elif comp_input == 'Rock' and user_input == 'Scissors':
            comp_win()
        elif comp_input == 'Paper' and user_input == 'Rock':
            comp_win()
        elif comp_input == 'Paper' and user_input == 'Paper':
            tie()
        elif comp_input == 'Paper' and user_input == 'Scissors':
            user_win()
        elif comp_input == 'Scissors' and user_input == 'Rock':
            user_win()
        elif comp_input == 'Scissors' and user_input == 'Paper':
            comp_win()
        elif comp_input == 'Scissors' and user_input == 'Scissors':
            tie()
        else:
            print("Please enter your choice correctly")
            pass
    except:
        print("Please enter your choice correctly")



