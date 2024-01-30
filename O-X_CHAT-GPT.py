import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.user_symbol = 'X'
        self.computer_symbol = 'O'
        self.current_player = self.user_symbol
        self.board = [' ' for _ in range(9)]
        self.buttons = []
        self.user_score = 0
        self.computer_score = 0

        # Create and configure the main frame
        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.grid(row=0, column=0)

        # Create and configure the score label
        self.score_label = tk.Label(self.main_frame, text=f"User: {self.user_score} | Computer: {self.computer_score}", font=('Arial', 12))
        self.score_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # Create and configure the buttons
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.main_frame, text='', font=('Arial', 14), width=8, height=3,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i + 1, column=j, padx=5, pady=5)
                self.buttons.append(button)

        # Create and configure the restart button
        self.restart_button = tk.Button(root, text="Restart", command=self.reset_game, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.restart_button.grid(row=1, column=0, pady=10)

        # Configure the main frame to expand on window resizing
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure([1, 2, 3], weight=1)

        # Configure root window
        self.root.configure(bg='#E0E0E0')

    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)
            if self.check_winner():
                if self.current_player == self.user_symbol:
                    self.user_score += 1
                else:
                    self.computer_score += 1
                self.show_result()
            elif ' ' not in self.board:
                for button in self.buttons:
                    button.config(bg='#FF0000')  # Change background to red
                self.show_result(draw=True)
            else:
                self.current_player = self.computer_symbol if self.current_player == self.user_symbol else self.user_symbol
                if self.current_player == self.computer_symbol:
                    self.computer_make_move()

    def computer_make_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == ' ']
        if empty_cells:
            move = random.choice(empty_cells)
            row, col = divmod(move, 3)
            self.make_move(row, col)

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ':
                self.highlight_winner_squares(i, i + 3, i + 6)
                return True  # Check rows
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != ' ':
                self.highlight_winner_squares(i * 3, i * 3 + 1, i * 3 + 2)
                return True  # Check columns

        if self.board[0] == self.board[4] == self.board[8] != ' ':
            self.highlight_winner_squares(0, 4, 8)
            return True  # Check diagonal (top-left to bottom-right)

        if self.board[2] == self.board[4] == self.board[6] != ' ':
            self.highlight_winner_squares(2, 4, 6)
            return True  # Check diagonal (top-right to bottom-left)

        return False

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = self.user_symbol

        for button in self.buttons:
            button.config(text='', state=tk.NORMAL, bg='#FFFFFF')  # Reset background color to default

        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

    def show_result(self, draw=False):
        if draw:
            messagebox.showinfo("Game Over", "Tie, no Winner")
        else:
            winner = "User" if self.current_player == self.user_symbol else "Computer"
            messagebox.showinfo("Game Over", f"{winner} wins!")
        self.reset_game()

    def highlight_winner_squares(self, *indices):
        for index in indices:
            self.buttons[index].config(bg='#0080FF')  # Change background to blue

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
