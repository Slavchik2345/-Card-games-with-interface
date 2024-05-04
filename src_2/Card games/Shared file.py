import tkinter as tk
import random
from tkinter import messagebox
def open_game1():
    class GuessGame(tk.Frame):
        def __init__(self, master):
            super().__init__(master)
            self.master = master
            self.pack()
            self.number = random.randint(1, 100)
            self.label = tk.Label(self, text=self.number)
            self.label.pack()
            self.up_button = tk.Button(self, text="Больше", command=self.up)
            self.up_button.pack()
            self.down_button = tk.Button(self, text="Меньше", command=self.down)
            self.down_button.pack()
            self.reset_button = tk.Button(self, text="Перезапустить", command=self.reset)
            self.reset_button.pack()
            self.status_label = None
        def up(self):
            new_number = random.randint(1, 100)
            self.label["text"] = new_number
            if new_number > self.number:
                self.win()
            else:
                self.lose()
        def down(self):
            new_number = random.randint(1, 100)
            self.label["text"] = new_number
            if new_number < self.number:
                self.win()
            else:
                self.lose()
        def win(self):
            self.up_button["state"] = "disabled"
            self.down_button["state"] = "disabled"
            self.status_label = tk.Label(self, text="Победа!")
            self.status_label.pack()
        def lose(self):
            self.up_button["state"] = "disabled"
            self.down_button["state"] = "disabled"
            self.status_label = tk.Label(self, text="Поражение!")
            self.status_label.pack()
        def reset(self):
            self.number = random.randint(1, 100)
            self.label["text"] = self.number
            self.up_button["state"] = "normal"
            self.down_button["state"] = "normal"
            if self.status_label is not None:
                self.status_label.destroy()
        root = tk.Tk()
        root.geometry("350x400")
        game = GuessGame(root)
        root.mainloop()

def open_game2():
    class Blackjack:
        def __init__(self, master):
            self.master = master
            self.master.title("Блекджек")
            self.deck = self.create_deck()
            self.player_hand = []
            self.dealer_hand = []
            self.player_total = 0
            self.dealer_total = 0
            self.create_widgets()
        def create_deck(self):
            return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        def deal_card(self):
            return self.deck.pop()
        def restart_game(self):
            self.player_hand = []
            self.dealer_hand = []
            self.player_total = 0
            self.dealer_total = 0
            self.dealer_label.config(text="Карты дилера: ")
        def hit(self):
            new_card = self.deal_card()
            self.player_hand.append(new_card)
            self.player_total = sum(self.player_hand)
            self.player_label.config(text="Карты игрока: {}".format(self.player_hand))
            if self.player_total > 21:
                messagebox.showinfo("Итог", "Бюст! Ты проиграл.")
            elif self.player_total == 21:
                self.stand()
        def stand(self):
            while self.dealer_total < 17:
                new_card = self.deal_card()
                self.dealer_hand.append(new_card)
                self.dealer_total = sum(self.dealer_hand)
            self.dealer_label.config(text="Карты дилера: {}".format(self.dealer_hand))
            if self.dealer_total > 21 or self.player_total > self.dealer_total:
                messagebox.showinfo("Итог", "Ты выйграл!")
            elif self.dealer_total > self.player_total:
                messagebox.showinfo("Итог", "Дилер выйграл.")
            else:
                messagebox.showinfo("Итог", "Это ничья!")
        def create_widgets(self):
            self.restart_button = tk.Button(self.master, text="Рестарт", command=self.restart_game)
            self.restart_button.pack()
            self.hit_button = tk.Button(self.master,text="Взять ещё", command=self.hit)
            self.hit_button.pack()
            self.stand_button = tk.Button(self.master, text="Вскрытие", command=self.stand)
            self.stand_button.pack()
            self.player_label = tk.Label(self.master, text="Карты игрока: ")
            self.player_label.pack()
            self.dealer_label = tk.Label(self.master, text="Карты дилера: ")
            self.dealer_label.pack()
    root = tk.Tk()
    root.geometry("350x400")
    game = Blackjack(root)
    root.mainloop()

root = tk.Tk()
root.title("Меню игр")
root.geometry("350x400")
button1 = tk.Button(root, text="Больше меньше", command=open_game1)
button1.pack()
button2 = tk.Button(root, text="Блекджек", command=open_game2)
button2.pack()
root.mainloop()