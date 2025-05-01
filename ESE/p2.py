# Q1: Two-Player Rock-Paper-Scissors Game

def play_game():
    # Rules for Rock-Paper-Scissors
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        # Get input from both players
        player1 = input("Player 1, enter your choice (rock, paper, or scissors): ").lower()
        player2 = input("Player 2, enter your choice (rock, paper, or scissors): ").lower()

        # Compare the players' choices and determine the winner
        if player1 == player2:
            print("It's a tie!")
        elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

        # Ask if players want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
play_game()

# Q2: Remove Duplicates from a List (Using Two Different Methods)
Method 1: Using a Loop to Remove Duplicates

def remove_duplicates_loop(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Test the function
test_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates_loop(test_list))  # Output: [1, 2, 3, 4, 5]
Method 2: Using a Set to Remove Duplicates
def remove_duplicates_set(lst):
    return list(set(lst))

# Test the function
test_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates_set(test_list))  # Output: [1, 2, 3, 4, 5] (order may vary)

# Q3: Reverse the Words in a String (Function Version)
def reverse_words():
    # Ask for input from the user
    string = input("Enter a long string with multiple words: ")

    # Split the string into words and reverse the list of words
    words = string.split()
    reversed_words = " ".join(reversed(words))

    # Print the reversed string
    print(f"Reversed string: {reversed_words}")

# Call the function to reverse the words
reverse_words()