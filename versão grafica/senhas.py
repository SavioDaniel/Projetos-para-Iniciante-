import random
import string
import tkinter as tk
from tkinter import messagebox

def gerador_de_senha(tamanho):
    gerador1 = string.ascii_letters 
    gerador2 = string.digits
    gerador3 = string.punctuation
    opcao = gerador1 + gerador2 + gerador3
    senha_usada = "".join(random.choice(opcao) for _ in range(tamanho))
    return senha_usada

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            raise ValueError
        senha = gerador_de_senha(tamanho)
        label_resultado.config(text=f"Senha gerada: {senha}", fg="#4CAF50")
        botao_copiar.config(state="normal")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o tamanho da senha.")

def copiar_senha():
    senha = label_resultado.cget("text").replace("Senha gerada: ", "")
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    janela.update()
    messagebox.showinfo("Copiar", "Senha copiada para a área de transferência!")

def sair():
    janela.destroy()

janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("500x350")
janela.configure(bg="#2E4053")

label_font = ("Arial", 14, "bold")
button_font = ("Arial", 12, "bold")

label_titulo = tk.Label(janela, text="Gerador de Senhas", font=("Arial", 20, "bold"), bg="#2E4053", fg="white")
label_titulo.pack(pady=10)

frame_input = tk.Frame(janela, bg="#2E4053")
frame_input.pack(pady=10)

label_instrucao = tk.Label(frame_input, text="Tamanho da senha:", font=label_font, bg="#2E4053", fg="white")
label_instrucao.grid(row=0, column=0, padx=5, pady=5)

entry_tamanho = tk.Entry(frame_input, width=10, font=("Arial", 14))
entry_tamanho.grid(row=0, column=1, padx=5, pady=5)

frame_botoes = tk.Frame(janela, bg="#2E4053")
frame_botoes.pack(pady=10)

botao_gerar = tk.Button(frame_botoes, text="Gerar Senha", font=button_font, bg="#4CAF50", fg="white", padx=20, pady=5, command=gerar_senha)
botao_gerar.grid(row=0, column=0, padx=10)

botao_sair = tk.Button(frame_botoes, text="Sair", font=button_font, bg="#E74C3C", fg="white", padx=20, pady=5, command=sair)
botao_sair.grid(row=0, column=1, padx=10)

botao_copiar = tk.Button(janela, text="Copiar Senha", font=button_font, bg="#3498DB", fg="white", padx=20, pady=5, state="disabled", command=copiar_senha)
botao_copiar.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 14), bg="#2E4053", fg="white", wraplength=450)
label_resultado.pack(pady=20)

janela.mainloop()
