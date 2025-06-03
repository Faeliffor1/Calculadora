import tkinter as tk 


janela = tk.Tk()
janela.title('Calculadora')

entrada = tk.Entry(janela, width=20 , font=('Arial', 20))
entrada.grid(row=0 , column=0 , columnspan=4)

# SALVANDO NO BANCO DE DADOS 

import sqlite3

conexao = sqlite3.connect('hitorico.db')
cursor = conexao.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
        expressao TEXT,
        resultado TEXT
    )
""")

conexao.commit()


def salvar_no_banco(expressao , resultado):
    cursor.execute("INSERT INTO historico (expressao, resultado) VALUES (?,?)", (expressao , resultado))
    conexao.commit()

# FUNÇOES DA CALCULADORA

def clicar(valor):
    entrada.insert(tk.END, valor) # adiciona o número no visor

def limpar():
    entrada.delete(0, tk.END) # apaga tudo no visor

def calcular():
    expressao = entrada.get() # pega o que está escrito
    try:
        resultado = str(eval(expressao)) # calcula o resultado
        entrada.delete(0, tk.END) # limpa o visor 
        entrada.insert(0, resultado) # mostra o resultado 
        salvar_no_banco(expressao , resultado) # salva no banco de dados 
    except:
        entrada.delete(0 , tk.END)
        entrada.insert(0 , 'ERRO')  

# BOTÕES DA CALCULADORA

botoes = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+',
]        

linha = 1
coluna = 0

for b in botoes:
    if b == '=':
        botao = tk.Button(janela, text= '=', width=5  , height=2 , command=calcular).grid(row=linha, column=coluna)
    else:
        botao = tk.Button(janela, text=b ,width=5 , height=2 , command=lambda x=b: clicar(x) ).grid(row=linha, column=coluna)

    #botao.grid(row=linha , column=coluna)     

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1 
tk.Button(janela , text='C' , width=22 , height=2 ,  command=limpar).grid(row=linha, column=0 , columnspan=4)

janela.mainloop()
