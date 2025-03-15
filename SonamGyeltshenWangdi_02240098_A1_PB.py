from random import randint

def guess_number_game():
    secret_number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    
    attempts = 0
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Correct! You got it in {attempts} tries!")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Enter a valid number.")





from random import choice

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    
    user_score = 0
    comp_score = 0
    
    print("Enter rock, paper, scissors or quit")
    
    while True:
        user = input("\nYour choice: ").lower()
        if user == "quit":
            break
        if user not in choices:
            print("Invalid choice!")
            continue
            
        comp = choice(choices)
        print(f"Computer: {comp}")
        
        if user == comp:
            print("Tie!")
        elif wins[user] == comp:
            print("You win!")
            user_score += 1
            break
        else:
            print("Computer wins!")
            comp_score += 1
            
        print(f"Score: You {user_score}, Computer {comp_score}")
    
    print(f"\nFinal: You {user_score}, Computer {comp_score}")



def main():
    while True :
        print("1. Guess Number Game : ")
        print("2. Rock Paper Scissor Game :")
        print("3. EXIT")
        choose = input ("Enter your CHOICE from 1 to 3 : ")
        if choose == '1':
            guess_number_game()
        elif choose == '2':
            rock_paper_scissors()
    
        
        elif choose =='3':
            print("EXITING")

    
        else:
            print("invalid")
        choose = input("do you want to play again (yes/no) : ").strip().lower()
        if choose != 'yes':
            print("thank you for playing")
            break
        
    
if __name__ == "__main__":
    main()


    