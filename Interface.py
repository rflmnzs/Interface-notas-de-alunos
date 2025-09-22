import tkinter as tk
def calcular_situacao():
    
    try:
        nome = entrada_nome.get()
        nota1 = float(entrada_nota1.get())
        nota2 = float(entrada_nota2.get())
        nota3 = float(entrada_nota3.get())
        
        if not all( 0 <= nota <= 10 for nota in [nota1, nota2, nota3]):
            resultado.config(text="Erro: as notas devem estar entre 0 e 10.", fg= "red")
            return
        
        media = (nota1 + nota2 + nota3)/3
        
        if media >= 7.0:
            situacao = "Aprovado"
            cor = "green"
        elif media >= 5.0:
            situacao = "Recuperação"
            cor = "orange"
        else:
            situacao = "Reprovado"
            cor = "red"

        resultado.config(  
          text=f"Aluno: {nome}\nMédia final: {media}\nSituação do aluno: {situacao}",
          fg=cor 
       )
       
    except ValueError:
        resultado.config(text="Por favor, insira notas válidas (números).", fg = "red")
        
janela = tk.Tk()
janela.title("Notas do aluno")
janela.geometry("350x320")
janela.configure(bg="#f0f0f0")

tk.Label(janela, text="Nome do Aluno:", bg="#f0f0f0").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Nota 1:", bg="#f0f0f0").pack()
entrada_nota1 = tk.Entry(janela)
entrada_nota1.pack()

tk.Label(janela, text="Nota 2:", bg="#f0f0f0").pack()
entrada_nota2 = tk.Entry(janela)
entrada_nota2.pack()

tk.Label(janela, text="Nota 3:", bg="#f0f0f0").pack()
entrada_nota3 = tk.Entry(janela)
entrada_nota3.pack()

tk.Button(janela, text="Calcular Situação", command=calcular_situacao).pack(pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 12), bg="#f0f0f0")
resultado.pack()
        
janela.mainloop()
