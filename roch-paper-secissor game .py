import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        # Initialize scores
        self.player_score = 0
        self.computer_score = 0
        self.tie_count = 0

        # Start the welcome screen
        self.welcome_screen()

    def welcome_screen(self):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Reset scores to zero on returning to the home page
        self.player_score = 0
        self.computer_score = 0
        self.tie_count = 0

        # Create a welcome message
        welcome_label = tk.Label(self.root, text="Welcome to Rock-Paper-Scissors Game!", font=("Arial", 20))
        welcome_label.pack(pady=40)

        # Enter button to start the game
        enter_button = tk.Button(self.root, text="Enter into the Game", font=("Arial", 14), command=self.start_game)
        enter_button.pack(pady=20)

    def start_game(self):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create the main game frame
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        # Game title
        self.label = tk.Label(frame, text="Choose Rock, Paper or Scissors", font=("Arial", 16))
        self.label.pack(pady=10)

        # Buttons for user choices
        self.rock_button = tk.Button(frame, text="Rock", width=15, command=lambda: self.play("Rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(frame, text="Paper", width=15, command=lambda: self.play("Paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(frame, text="Scissors", width=15, command=lambda: self.play("Scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        # Label to display the result
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        # Labels to display scores
        self.score_label = tk.Label(self.root, text=f"Player: {self.player_score}  |  Computer: {self.computer_score}  |  Ties: {self.tie_count}", font=("Arial", 12))
        self.score_label.pack(pady=10)

    def play(self, player_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        # Determine the winner and update scores
        if player_choice == computer_choice:
            result = "It's a tie!"
            self.tie_count += 1
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        # Update the result label
        self.result_label.config(text=f"You chose {player_choice}, Computer chose {computer_choice}.\n{result}")
        
        # Update the score label
        self.score_label.config(text=f"Player: {self.player_score}  |  Computer: {self.computer_score}  |  Ties: {self.tie_count}")

        # Show the result in a messagebox and ask if the player wants to play again
        self.play_again(result, player_choice, computer_choice)

    def play_again(self, result, player_choice, computer_choice):
        messagebox.showinfo("Result", f"You chose {player_choice}\nComputer chose {computer_choice}\n{result}")
        again = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if again:
            self.start_game()  # Restart the game if the user wants to play again
        else:
            self.welcome_screen()  # Return to home page if the user doesn't want to play again


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
