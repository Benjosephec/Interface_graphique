import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Devinette")
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.points = 0
        
        self.label = tk.Label(root, text="Devinez un nombre entre 1 et 100", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=5)
        
        self.points_label = tk.Label(root, text=f"Points : {self.points}", font=("Arial", 12), fg="green")
        self.points_label.pack(pady=5)
        
        self.check_button = tk.Button(root, text="Vérifier", font=("Arial", 14), command=self.check_guess)
        self.check_button.pack(pady=10)
        
        self.reset_button = tk.Button(root, text="Réinitialiser", font=("Arial", 12), command=self.reset_game)
        self.reset_button.pack(pady=10)
        self.reset_button.config(state="disabled")
        
    def calculate_points(self):
        return max(100 - (self.attempts - 1) * 10, 10)
    
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess < self.number_to_guess:
                self.result_label.config(text="Plus grand !", fg="orange")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Plus petit !", fg="orange")
            else:
                points_won = self.calculate_points()
                self.points += points_won
                self.result_label.config(text=f"Bravo ! Vous avez trouvé en {self.attempts} essais. (+{points_won} points)", fg="green")
                self.points_label.config(text=f"Points : {self.points}")
                self.check_button.config(state="disabled")
                self.reset_button.config(state="normal")
        except ValueError:
            self.result_label.config(text="Veuillez entrer un nombre valide.", fg="red")
    
    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.check_button.config(state="normal")
        self.reset_button.config(state="disabled")

root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
