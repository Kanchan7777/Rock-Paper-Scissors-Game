import tkinter as tk
import random

# Game logic
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Update UI on button press
def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=f"Result: {result}")

    if result == "You Win!":
        scores['user'] += 1
    elif result == "Computer Wins!":
        scores['computer'] += 1

    score_label.config(text=f"Score - You: {scores['user']} | Computer: {scores['computer']}")

# Reset game
def reset_game():
    scores['user'] = 0
    scores['computer'] = 0
    user_choice_label.config(text="You chose:")
    computer_choice_label.config(text="Computer chose:")
    result_label.config(text="Result:")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Initialize scores
scores = {"user": 0, "computer": 0}

# Create UI
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Labels
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 14)).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

# Buttons
tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

user_choice_label = tk.Label(root, text="You chose:", font=("Helvetica", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer chose:", font=("Helvetica", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Result:", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12))
score_label.pack(pady=10)

tk.Button(root, text="Reset Game", command=reset_game).pack(pady=10)

# Run the GUI
root.mainloop()