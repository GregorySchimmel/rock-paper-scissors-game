import random  # This lets us make random choices for the computer

print("Welcome to Rock-Paper-Scissors! Type 'quit' to exit.")


    # Computer's choice next
while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice == 'quit':
        print("Thanks for playing!")
        break
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Try again.")
        continue  # Skip to next loop iteration
    
    # Computer chooses randomly
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # Winner logic next
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")
