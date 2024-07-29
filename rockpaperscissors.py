import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self,root):
        self.root=root
        self.root.title("Rock Paper Scissors Game")

        # Add a heading label
        self.heading_label=tk.Label(root,text="Rock Paper Scissors Game",font=("Helvetica",24))
        self.heading_label.pack(pady=20)

       # Rounds input section
        self.rounds_label=tk.Label(root,text="Enter number of rounds:",font=("Comic Sans MS",15))
        self.rounds_label.pack(pady=10)

        self.round_entry=tk.Entry(root,font=("Comic Sans MS",15))
        self.round_entry.pack(pady=10)

        # Start button
        self.start_button=tk.Button(root,text="Start Game",font=("Comic Sans MS",15),command=self.start_game)
        self.start_button.config(bg="Beige",fg="Dark Green")
        self.start_button.pack(pady=10)

        # Rounds info label
        self.rounds_info_label=tk.Label(root,text="",font=("Comic Sans MS",15))
        self.rounds_info_label.pack(pady=10)

        # Button Frame
        self.button_frame=tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Rock button
        self.rock_button=tk.Button(self.button_frame,text="Rock",font=("Comic Sans MS",12),command=lambda:self.play("rock"),state=tk.DISABLED)
        self.rock_button.config(bg="Black",fg="Tan")
        self.rock_button.pack(side=tk.LEFT,padx=10)

        # Paper button
        self.paper_button=tk.Button(self.button_frame,text="Paper",font=("Comic Sans MS",12),command=lambda:self.play("paper"),state=tk.DISABLED)
        self.paper_button.config(bg="Black",fg="Tan")
        self.paper_button.pack(side=tk.LEFT,padx=10)

        # Scissors button
        self.scissors_button=tk.Button(self.button_frame,text="Scissors",font=("Comic Sans MS",12),command=lambda:self.play("scissors"),state=tk.DISABLED)
        self.scissors_button.config(bg="Black",fg="Tan")
        self.scissors_button.pack(side=tk.LEFT,padx=10)

        # Result and Score label
        self.result_label=tk.Label(root,text="",font=("Comic Sans MS",16))
        self.result_label.pack(pady=20)

        self.score_label=tk.Label(root,text="",font=("Comic Sans MS",16))
        self.score_label.pack(pady=20)

        # Play Again button
        self.play_again_button=tk.Button(root,text="Play Again",font=("Comic Sans MS",12),command=self.reset_game,state=tk.DISABLED)
        self.play_again_button.config(bg="Black",fg="Olive")
        self.play_again_button.pack(pady=20)

    def start_game(self):
        self.rounds_to_play=int(self.round_entry.get())
        self.rounds_played =  0
        self.user_score = 0
        self.computer_score = 0

        # Update rounds info label
        self.rounds_info_label.config(text=f"Number Of Rounds: {self.rounds_to_play}",bg="Yellow")

        self.result_label.config(text="")
        self.score_label.config(text="Score: You: 0 | Computer: 0")

        self.round_entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)

        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)

    def play(self,user_choice):
        computer_choice=random.choice(["rock","paper","scissors"])
        result = self.determine_winner(user_choice,computer_choice)

        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

        if result == "You Win!":
            self.user_score+=1
        elif result== "You Lose!":
            self.computer_score+=1

        self.rounds_played+=1
        self.score_label.config(text=f"Score: You: {self.user_score} | Computer: {self.computer_score}")

        if self.rounds_played>= self.rounds_to_play:
            self.end_game()

    def determine_winner(self,user_choice,computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or\
             (user_choice == "scissors" and computer_choice == "paper") or\
             (user_choice == "paper" and computer_choice == "rock"):
            return "You Win!"
        else:
            return "You Lose!"

    def end_game(self):
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)

        self.play_again_button.config(state=tk.NORMAL)
        self.round_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)

        if self.user_score > self.computer_score:
            self.result_label.config(text="Game Over! You are the champion!", fg="red")
        elif self.user_score < self.computer_score:
            self.result_label.config(text="Game Over! Computer Wins!", fg="red")
        else:
            self.result_label.config(text="Game Over! It's a tie!",fg="red")

    def reset_game(self):
        self.user_score=0
        self.computer_score=0
        self.rounds_played=0
        self.result_label.config(text="")
        self.score_label.config(text="Score: You: 0 | Computer: 0")
        self.rounds_info_label.config(text="Number of Rounds:")
        
        self.play_again_button.config(state=tk.DISABLED)
        self.round_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        
#Run the application/code
root=tk.Tk()
game= RockPaperScissorsGame(root)
root.mainloop()





