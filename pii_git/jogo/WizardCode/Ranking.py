from tkinter import *
from tkinter import ttk
import sqlite3

#variaveis globais
conn = None
janela = None
conn = sqlite3.connect("ranking.sql")
c = conn.cursor()

def fechar_janela_anterior():
    global janela
    if janela is not None:
        janela.destroy()


def inserir_dados():
    from WizardCode import nome, email
    from WizardCodeJogo import temp
    c.execute("""INSERT INTO Ranking (nome, email, Tempo_total) VALUES (?,?,?)""",(nome, email, temp))
    conn.commit()


    
janela = Tk()
janela.title("Ranking")
janela.geometry("600x560+610+153")

janela.configure(bg="light green")
label_wizard_code = Label(janela, text="RANKING", bd=3, font=("TIMES", 30), fg="white", bg="lightslateblue")
label_wizard_code.pack(pady=30)


#def popular():
    #vquery="SELECT * FROM Ranking ORDER BY Tempo_total ASC"
    #linhas=ranking.dql(vquery)#######

quadroGrid =LabelFrame(janela, text="Tabela")
quadroGrid.pack(fill="both",expand="yes",padx=60,pady=90)
tv=ttk.Treeview(quadroGrid, columns=("Nome","Email", "Tempo"), show="headings")
tv.column("Nome", minwidth=0, width=100)
tv.column("Email", minwidth=0, width=250)
tv.column("Tempo", minwidth=0, width=100)
tv.heading("Nome", text="Nome")
tv.heading("Email", text="Email")
tv.heading("Tempo", text="Tempo")
tv.pack()

# incia a janela principal (janela)
janela.mainloop()

def my_sort(col):
    global df,order
    if order == False:
        order == True
    df=df.sort_values(by=[col], ascending=order)