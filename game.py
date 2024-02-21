import tkinter as tk
from tkinter import messagebox
import random

class Game:
    def _init_(self, master):
        self.master = master
        self.master.title("Game Batu Gunting Kertas")
        self.master.geometry("300x250")

        self.choices = ["Batu", "Gunting", "Kertas"]
        self.chances_left = 3

        self.user_label = tk.Label(self.master, text="Pilihan Anda: ")
        self.user_label.pack()

        self.user_choice = tk.StringVar()
        self.user_choice.set(self.choices[0])

        self.user_menu = tk.OptionMenu(self.master, self.user_choice, *self.choices)
        self.user_menu.pack()

        self.hint_button = tk.Button(self.master, text="Hint", command=self.show_hint)
        self.hint_button.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.play_game)
        self.submit_button.pack()

    def show_hint(self):
        hint = "Hint: "
        hint += "Batu menghancurkan Gunting, "
        hint += "Gunting memotong Kertas, "
        hint += "Kertas melipat Batu."
        messagebox.showinfo("Hint", hint)

    def play_game(self):
        computer_choice = random.choice(self.choices)
        user_choice = self.user_choice.get()

        result_text = f"Anda memilih: {user_choice}\nKomputer memilih: {computer_choice}\n"

        if user_choice == computer_choice:
            result_text += "Hasil: Seri!"
        elif (
            (user_choice == "Batu" and computer_choice == "Gunting") or
            (user_choice == "Gunting" and computer_choice == "Kertas") or
            (user_choice == "Kertas" and computer_choice == "Batu")
        ):
            result_text += "Hasil: Anda Menang!"
        else:
            result_text += "Hasil: Anda Kalah!"

        self.show_result(result_text)

        self.chances_left -= 1
        if self.chances_left == 0:
            messagebox.showinfo("Game Over", "Anda telah kehabisan kesempatan. Game over!")
            self.master.destroy()
        else:
            messagebox.showinfo("Kesempatan Tersisa", f"Anda memiliki {self.chances_left} kesempatan lagi.")

    def show_result(self, result_text):
        result_window = tk.Toplevel(self.master)
        result_window.title("Hasil")
        result_label = tk.Label(result_window, text=result_text)
        result_label.pack()
        close_button = tk.Button(result_window, text="Tutup", command=result_window.destroy)
        close_button.pack()

if _name_ == "_main_":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()