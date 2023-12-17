import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror(
            "Erro", "Por favor, insira um número válido para o comprimento.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    strength = min(length / 20, 1)

    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

    security_indicator.config(bg=get_security_color(strength))


def get_security_color(strength):
    if strength < 0.3:
        return "red"
    elif strength < 0.7:
        return "orange"
    else:
        return "green"


def toggle_password_visibility():
    current_state = password_entry.cget("show")
    password_entry.config(show="" if current_state else "*")


root = tk.Tk()
root.title("Gerador de Senhas Aleatórias")

length_var = tk.StringVar()
length_var.set("12")

length_label = tk.Label(root, text="Comprimento da Senha:")
length_label.pack()

length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()

generate_button = tk.Button(
    root, text="Gerar Senha", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="Senha Gerada:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

show_password_button = tk.Button(
    root, text="Mostrar/Ocultar Senha", command=toggle_password_visibility)
show_password_button.pack()

security_indicator = tk.Label(root, text="Força da Senha", width=20)
security_indicator.pack()

root.mainloop()
