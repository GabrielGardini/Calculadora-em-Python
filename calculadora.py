from tkinter import *
from tkinter import ttk

AZUL = "#A0E7E1"
ROXO = "#480C7A"
AZUL_ESCURO="#6153CC"
PELE="#E0AFA0"
ROSA="#FFACE4"
VERDE="#C1FF9B"

class Window:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculadora em python')
        self.master.geometry("300x300") #tamanho da janela
        self.master.maxsize(300,300)
        self.master.configure(background=AZUL) #cor de fundo 

        self.nb=ttk.Notebook(master)
        self.nb.place(x=0,y=0,width=300,height=300)

        self.calculadora = Calculadora(self.nb)
        self.min_to_h = MinutosParaHoras(self.nb)
        self.conv = ConvCelsius(self.nb)

class Calculadora:
    def __init__(self, notebook) -> None:
        
        self.tela = Frame(notebook)
        notebook.add(self.tela, text='Calculadora')
        self.tela.configure(background=AZUL)

        self.txt1=Label(self.tela,text="Calculadora em Python :)", font=("Times New Roman Baltic", 11),background =AZUL,foreground= ROXO)
        self.txt1.place(x=65,y=10,width=170,height=30)

        self.entrada1=Entry(self.tela, font=("Times New Roman Baltic", 10))
        self.entrada1.place(x=75,y=50,width=150,height=30)

        self.entrada2=Entry(self.tela,font=("Times New Roman Baltic", 10))
        self.entrada2.place(x=75,y=90,width=150,height=30)

        self.btnsoma = Button(self.tela,text="+",command = self.soma,  bg=ROXO,fg="#FFF")
        self.btnsoma.place(x=75,y=130,width=30,height=30)

        self.btnsubtração = Button(self.tela,text="-",command = self.subtrair,  bg=ROXO,fg="#FFF")
        self.btnsubtração.place(x=105,y=130,width=30,height=30)

        self.btnmult = Button(self.tela,text="X",command = self.multiplicar, bg=ROXO,fg="#FFF")
        self.btnmult.place(x=135,y=130,width=30,height=30)

        self.btndivisao = Button(self.tela,text="/",command = self.dividir, bg=ROXO,fg="#FFF")
        self.btndivisao.place(x=165,y=130,width=30,height=30)

        self.btnelevar = Button(self.tela,text="^",command = self.elevar, bg=ROXO,fg="#FFF")
        self.btnelevar.place(x=195,y=130,width=30,height=30)

        self.resultadofinal=Label(self.tela,text="Resultado: ",font=("Times New Roman Baltic", 10, "bold"),background =AZUL,foreground= ROXO)
        self.resultadofinal.place(x=25,y=180,width=250,height=30)

        self.creditos = Label(self.tela, text="Criado por Gabriel Gardini \n @ggardini1",font=("Times New Roman Baltic", 9), bg=AZUL, fg=ROXO)
        self.creditos.place(x=75,y=230,width=160,height=30)

    def soma(self):
        x = float(self.entrada1.get())
        y = float(self.entrada2.get())
        resultado_conta= x+y

        self.resultadofinal["text"] = f"Resultado: {resultado_conta}"

    def subtrair(self):
        x = float(self.entrada1.get())
        y = float(self.entrada2.get())
        resultado_conta= x-y

        self.resultadofinal["text"] = f"Resultado: {resultado_conta}"

    def multiplicar(self):
        x = float(self.entrada1.get())
        y = float(self.entrada2.get())
        resultado_conta= x*y

        self.resultadofinal["text"] = f"Resultado: {resultado_conta:.3f}"

    def dividir(self):
        x = float(self.entrada1.get())
        y = float(self.entrada2.get())
        resultado_conta= x/y

        self.resultadofinal["text"] = f"Resultado: {resultado_conta:.3f}"

    def elevar(self):
        x = float(self.entrada1.get())
        y = float(self.entrada2.get())
        resultado_conta= x**y

        self.resultadofinal["text"] = f"Resultado: {resultado_conta}"

class MinutosParaHoras:

    def __init__(self, notebook) -> None:
        self.tela=Frame(notebook)
        notebook.add(self.tela,text="Conversor min/h")
        self.tela.configure(background=VERDE) #cor de fundo 
        self.info_conversor = Label(self.tela, text="Digite um valor em \n minutos ou horas:",font=("Times New Roman Baltic", 11),bg=VERDE,fg="black" )
        self.info_conversor.place(x=75,y=10,width=150,height=50)

        self.entrada_min= Entry(self.tela,font=("Times New Roman Baltic", 11), bg="white")
        self.entrada_min.place(x=75,y=90,width=150,height=30)

        self.btn_min_h= Button(self.tela, text="Min -> h",font=("Times New Roman Baltic",10 ), bg=ROSA, command=self.conv_min_h)
        self.btn_min_h.place(x=75,y=140,width=74,height=20)

        self.btn_h_min= Button(self.tela, text="h -> Min",font=("Times New Roman Baltic" ,10), bg=ROSA, command=self.conv_h_min)
        self.btn_h_min.place(x=150,y=140,width=74,height=20)

        self.result=Label(self.tela, text=" ",font=("Times New Roman Baltic ",10, "bold"),bg=VERDE)
        self.result.place(x=60,y=180,width=180,height=30)

        self.creditos_t2 = Label(self.tela, text="Criado por Gabriel Gardini \n @ggardini1",font=("Times New Roman Baltic", 9), bg=VERDE, fg="black")
        self.creditos_t2.place(x=75,y=230,width=160,height=30)

    def conv_min_h(self):
        x=float(self.entrada_min.get())
        horas= x/60
        self.result["text"] = f"{horas:.3f} horas."
        self.result["bg"] = VERDE

    def conv_h_min(self):
        x=float(self.entrada_min.get())
        horas= x*60
        self.result["text"] = f"{horas:.3f} minutos."
        self.result["bg"] = VERDE

class ConvCelsius:
    def __init__(self, notebook) -> None:
        self.tela=Frame(notebook)
        notebook.add(self.tela,text="Conversor Celsius/ºF")
        self.tela.configure(background=AZUL_ESCURO) #cor de fundo 

        self.info_conversor_temperatura = Label(self.tela, text="Digite um valor em \n Celsius ou\n Fahrenheit:",font=("Times New Roman Baltic", 11),bg=AZUL_ESCURO,fg="white" )
        self.info_conversor_temperatura.place(x=75,y=10,width=150,height=60)

        self.entrada_temperatura= Entry(self.tela,font=("Times New Roman Baltic", 11), bg="white")
        self.entrada_temperatura.place(x=75,y=90,width=150,height=30)

        self.btn_C_F= Button(self.tela, text="ºC -> ºF",font=("Times New Roman Baltic",10 ), bg=PELE, command=self.conv_C_F)
        self.btn_C_F.place(x=75,y=140,width=74,height=20)

        self.btn_F_C= Button(self.tela, text="ºF -> ºC",font=("Times New Roman Baltic" ,10), bg=PELE, command=self.conv_F_C)
        self.btn_F_C.place(x=150,y=140,width=74,height=20)

        self.result_temp=Label(self.tela, text=" ",font=("Times New Roman Baltic", 10, "bold"),bg=AZUL_ESCURO,fg="white")
        self.result_temp.place(x=60,y=180,width=180,height=30)

        self.creditos_t3 = Label(self.tela, text="Criado por Gabriel Gardini \n @ggardini1",font=("Times New Roman Baltic", 9), bg=AZUL_ESCURO, fg="white")
        self.creditos_t3.place(x=75,y=230,width=160,height=30)

    def conv_F_C(self):
        F=float(self.entrada_temperatura.get())
        C= (F-32)/1.8
        self.result_temp["text"] = f"{C:.3f} Graus Celsius."
        self.result_temp["bg"] = AZUL_ESCURO

    def conv_C_F(self):
        C=float(self.entrada_temperatura.get())
        F= (C*1.8)+32
        self.result_temp["text"] = f"{F:.3f} Graus Fahrenheit."
        self.result_temp["bg"] = AZUL_ESCURO
        
def main():
    janela = Tk()
    app = Window(janela)
    janela.mainloop()

if __name__ == '__main__':
    main()
