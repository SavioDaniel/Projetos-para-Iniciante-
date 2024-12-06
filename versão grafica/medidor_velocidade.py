import tkinter as tk
from tkinter import messagebox

def verificar_velocidade():
    try:
        # Obter o valor da velocidade
        velocidade = float(velocidade_entry.get())

        # Verificação de valores
        if velocidade < 0:
            messagebox.showerror("Erro", f"Velocidade inválida: {velocidade}. Não existe velocidade negativa!")
            return
        elif velocidade <= 80:
            messagebox.showinfo("Resultado", f"Você não recebeu multa. Sua velocidade era {velocidade} km/h, dentro do limite permitido de 80 km/h.")
        elif 81 <= velocidade <= 90:
            messagebox.showwarning("Multa leve", f"Velocidade registrada: {velocidade} km/h.\nVocê receberá uma multa leve.")
        elif 91 <= velocidade <= 100:
            messagebox.showwarning("Multa grave", f"Velocidade registrada: {velocidade} km/h.\nVocê receberá uma multa grave.")
        else:
            messagebox.showerror("Multa gravíssima", f"Velocidade registrada: {velocidade} km/h.\nVocê receberá uma multa gravíssima.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para a velocidade.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Verificador de Velocidade")
janela.geometry("400x200")

# Label e campo de entrada para velocidade
tk.Label(janela, text="Digite a velocidade do veículo (km/h):").pack(pady=10)
velocidade_entry = tk.Entry(janela, width=20)
velocidade_entry.pack()

# Botão para verificar velocidade
tk.Button(janela, text="Verificar", command=verificar_velocidade).pack(pady=20)

# Rodar o app
janela.mainloop()
