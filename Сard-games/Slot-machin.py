from tkinter import *
from tkinter import messagebox
import random

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

