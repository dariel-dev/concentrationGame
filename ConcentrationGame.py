import tkinter as tk
from tkinter import messagebox
import random


class ConcentrationGame:
    def __init__(self, root):
        # Game settings
        self.ROWS = 4
        self.COLUMNS = 5
        self.TOTAL_CARDS = self.ROWS * self.COLUMNS
        self.TOTAL_PAIRS = self.TOTAL_CARDS // 2
        self.BACK_COLOR = 'green'  # Initial button color set to green
        self.REVEALED_COLOR = 'white'
        self.MATCHED_COLOR = 'green'
        self.FONT = ('Helvetica', 20, 'bold')  # Increased font size

        # Initialize game state
        self.cards = []
        self.values = list(range(self.TOTAL_PAIRS)) * 2
        random.shuffle(self.values)
        self.first_card = None
        self.second_card = None
        self.pairs_found = 0
        self.waiting_for_second_card = False

        # Setup the root window
        root.title("Concentration Game")

        # Create the buttons (cards) and add them to the grid
        for i in range(self.TOTAL_CARDS):
            button = tk.Button(root, width=8, height=4, bg=self.BACK_COLOR, fg='black', font=self.FONT,
                               command=lambda i=i: self.on_card_click(i))
            button.grid(row=i // self.COLUMNS, column=i % self.COLUMNS)
            self.cards.append(button)

    def on_card_click(self, index):
        clicked_card = self.cards[index]

        if not self.waiting_for_second_card:
            # First card is clicked
            self.first_card = index
            clicked_card.config(text=str(self.values[index]), bg=self.REVEALED_COLOR)
            self.waiting_for_second_card = True
        else:
            # Second card is clicked
            self.second_card = index
            clicked_card.config(text=str(self.values[index]), bg=self.REVEALED_COLOR)
            self.waiting_for_second_card = False
            self.check_match()

    def check_match(self):
        if self.values[self.first_card] == self.values[self.second_card]:
            # Cards match
            self.cards[self.first_card].config(bg=self.MATCHED_COLOR, state='disabled')
            self.cards[self.second_card].config(bg=self.MATCHED_COLOR, state='disabled')
            self.pairs_found += 1

            if self.pairs_found == self.TOTAL_PAIRS:
                self.show_game_over_message()
        else:
            # No match, hide cards after a delay
            self.cards[self.first_card].after(1000, self.hide_cards, self.first_card, self.second_card)

    def hide_cards(self, first, second):
        self.cards[first].config(text="", bg=self.BACK_COLOR)
        self.cards[second].config(text="", bg=self.BACK_COLOR)

    def show_game_over_message(self):
        messagebox.showinfo("Congratulations", "You won!")


if __name__ == "__main__":
    root = tk.Tk()
    game = ConcentrationGame(root)
    root.mainloop()

