import tkinter as tk
from tkinter import messagebox

def calcular_fatorial():
    try:
        # Obter o número inserido
        num = int(numero_entry.get())

        if num == -10:
            messagebox.showinfo("Encerrar", "Você saiu do programa.")
            janela.destroy()
        elif num < 0:
            messagebox.showerror("Erro", "Número inválido. Não é possível calcular o fatorial de números negativos.")
        elif num == 0:
            messagebox.showinfo("Resultado", f"O fatorial de {num} é 1.")
        else:
            # Calcular o fatorial
            fatorial = 1
            for i in range(1, num + 1):
                fatorial *= i
            messagebox.showinfo("Resultado", f"O fatorial de {num} é {fatorial}.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Fatorial")
janela.geometry("400x200")

# Label e campo de entrada para o número
tk.Label(janela, text="Digite um número (diferente de -10 para continuar):").pack(pady=10)
numero_entry = tk.Entry(janela, width=20)
numero_entry.pack()

# Botão para calcular o fatorial
tk.Button(janela, text="Calcular", command=calcular_fatorial).pack(pady=20)

# Rodar o app
janela.mainloop()
