import tkinter as tk
import random
from tkinter import messagebox
from tkinter import *
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

def open_game3():
    class SlotMachine:
        def __init__(self, master):
            self.master = master
            self.master.title("Игровой автомат")

            self.balance = 100  # Изначальный баланс игрока

            self.display = Label(master, text="", font=("Helvetica", 48))
            self.display.pack(pady=20)

            self.spin_button = Button(master, text="Крутить ($15)", command=self.spin)
            self.spin_button.pack(pady=10)

            self.result = Label(master, text="", font=("Helvetica", 24))
            self.result.pack(pady=10)

        def spin(self):
            if self.balance < 15:
                self.open_payment_window()
                return

            self.balance -= 15

            numbers = [random.randint(0, 9) for _ in range(3)]
            self.display.config(text=" ".join(map(str, numbers)))

            if numbers[0] == numbers[1] == numbers[2]:
                self.balance += 30
                self.result.config(text="ПОБЕДА! Вы выиграли $30!")
            else:
                self.result.config(text="ПОРАЖЕНИЕ! У вас осталось ${} на балансе.".format(self.balance))

        def open_payment_window(self):
            payment_window = Toplevel(self.master)
            payment_window.title("Пополнение баланса")

            card_number_label = Label(payment_window, text="Номер карты:")
            card_number_label.grid(row=0, column=0)
            card_number_entry = Entry(payment_window)
            card_number_entry.grid(row=0, column=1)

            expiration_date_label = Label(payment_window, text="Срок действия:")
            expiration_date_label.grid(row=1, column=0)
            expiration_date_entry = Entry(payment_window)
            expiration_date_entry.grid(row=1, column=1)

            cvv_label = Label(payment_window, text="CVV:")
            cvv_label.grid(row=2, column=0)
            cvv_entry = Entry(payment_window)
            cvv_entry.grid(row=2, column=1)

            def add_funds():
                nonlocal payment_window
                card_number = card_number_entry.get()
                expiration_date = expiration_date_entry.get()
                cvv = cvv_entry.get()
                self.balance = self.balance + 100

                # Здесь должен быть код для обработки платежа

                messagebox.showinfo("Пополнение баланса", "Баланс успешно пополнен!")
                payment_window.destroy()

            add_funds_button = Button(payment_window, text="Пополнить баланс", command=add_funds)
            add_funds_button.grid(row=3, columnspan=2, pady=10)

    root = Tk()
    slot_machine = SlotMachine(root)
    root.mainloop()

root = tk.Tk()
root.title("Меню игр")
root.geometry("350x400")
button1 = tk.Button(root, text="Больше меньше", command=open_game1)
button1.pack()
button2 = tk.Button(root, text="Блекджек", command=open_game2)
button2.pack()
button3 = tk.Button(root, text="Игровой автомат", command=open_game3)
button3.pack()
root.mainloop()
