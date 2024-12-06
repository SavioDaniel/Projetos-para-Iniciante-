import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        idade = int(idade_entry.get())
        sexo = sexo_entry.get().upper()
        peso = float(peso_entry.get())
        altura = float(altura_entry.get())

        if idade < 0 or peso <= 0 or altura <= 0:
            messagebox.showerror("Erro", "Por favor, insira valores positivos para idade, peso e altura.")
            return
        if sexo not in ['M', 'F']:
            messagebox.showerror("Erro", "Sexo inválido! Use 'M' para masculino ou 'F' para feminino.")
            return

        imc = peso / (altura ** 2)
        faixa_etaria = "criança" if idade <= 18 else "adulto"

        if faixa_etaria == "criança":
            if sexo == 'M':
                tabela = """Tabela para crianças do sexo masculino:
Abaixo de 16,5: Abaixo do peso
16,5 - 22,9: Peso normal
23 - 26,9: Sobrepeso
27 ou mais: Obesidade"""
            else:
                tabela = """Tabela para crianças do sexo feminino:
Abaixo de 15,5: Abaixo do peso
15,5 - 21,9: Peso normal
22 - 25,9: Sobrepeso
26 ou mais: Obesidade"""
        else:
            if sexo == 'M':
                tabela = """Tabela para adultos do sexo masculino:
Abaixo de 18,5: Abaixo do peso
18,5 - 24,9: Peso normal
25 - 29,9: Sobrepeso
30 ou mais: Obesidade"""
            else:
                tabela = """Tabela para adultos do sexo feminino:
Abaixo de 17,5: Abaixo do peso
17,5 - 23,9: Peso normal
24 - 28,9: Sobrepeso
29 ou mais: Obesidade"""

        resultado = f"Você é um(a) {faixa_etaria}.\n"
        resultado += f"IMC: {imc:.2f}\n"
        resultado += f"{tabela}"
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de inserir números válidos para idade, peso e altura.")

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("500x500")
janela.configure(bg="#2C3E50")

title_label = tk.Label(janela, text="Calculadora de IMC", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=20)

frame = tk.Frame(janela, bg="#34495E")
frame.pack(pady=10, padx=10, fill="both", expand=True)

tk.Label(frame, text="Idade:", font=("Arial", 12), bg="#34495E", fg="white").grid(row=0, column=0, pady=10, padx=10, sticky="e")
idade_entry = tk.Entry(frame, font=("Arial", 12), width=10)
idade_entry.grid(row=0, column=1, pady=10, padx=10)

tk.Label(frame, text="Sexo (M/F):", font=("Arial", 12), bg="#34495E", fg="white").grid(row=1, column=0, pady=10, padx=10, sticky="e")
sexo_entry = tk.Entry(frame, font=("Arial", 12), width=10)
sexo_entry.grid(row=1, column=1, pady=10, padx=10)

tk.Label(frame, text="Peso (kg):", font=("Arial", 12), bg="#34495E", fg="white").grid(row=2, column=0, pady=10, padx=10, sticky="e")
peso_entry = tk.Entry(frame, font=("Arial", 12), width=10)
peso_entry.grid(row=2, column=1, pady=10, padx=10)

tk.Label(frame, text="Altura (m):", font=("Arial", 12), bg="#34495E", fg="white").grid(row=3, column=0, pady=10, padx=10, sticky="e")
altura_entry = tk.Entry(frame, font=("Arial", 12), width=10)
altura_entry.grid(row=3, column=1, pady=10, padx=10)

botao_calcular = tk.Button(janela, text="Calcular IMC", font=("Arial", 14), bg="#1ABC9C", fg="white", command=calcular_imc)
botao_calcular.pack(pady=20)

janela.mainloop()


