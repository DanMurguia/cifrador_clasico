import affine_vignere
from tkinter import *
import tkinter as tk
import interfaz_affine
import interfaz_vignere
import interfaz_aee

class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.parent = parent
            
        self.parent.title("Cifrador")
        
        self.var_selected = IntVar()
        
        self.parent.geometry('640x480')
        
        self.configure(bg='NavajoWhite2')
        
        labl = Label(self,text="ELIJA UN ALGORITMO", 
                     font=('comic sans ms',25,'bold'), background='NavajoWhite2')
        
        labl.grid(row=0,column=0, padx=120)
        
        rad0 = Radiobutton(self,text='Algoritmo Extendido de Euclides', value=1,
                           font=('Helvetica',18,'bold italic'), 
                           background='NavajoWhite2',variable=self.var_selected)
        
        rad1 = Radiobutton(self,text='Cifrado Affine', value=2,
                           font=('Helvetica',18,'bold italic'), 
                           background='NavajoWhite2',variable=self.var_selected)
        
        rad2 = Radiobutton(self,text='Cifrado Vigenère', value=3,
                           font=('Helvetica',18,'bold italic'),
                           background='NavajoWhite2',variable=self.var_selected)
       
        rad0.grid(row=1, column=0, pady=40)
        rad1.grid(row=2, column=0)
        rad2.grid(row=3, column=0, pady=40)
        
        bt = Button(self,text='Seleccionar', command = self.select,
                    width = 20, height = 2, font=('Helvetica',15), 
                    background= 'saddle brown', foreground='white')
        
        bt.grid(row = 4, column = 0, pady=20)
        
        
        
    def select(self):
        if(self.var_selected.get() == 1):
            interfaz_aee.VentanaAEE(self.parent, "Algoritmo Extendido de Euclides")
        elif( self.var_selected.get() == 2):
            interfaz_affine.VentanaAffine(self.parent, "Cifrado Affine")
        elif(self.var_selected.get()==3):
            interfaz_vignere.VentanaVigenere(self.parent, "Cifrado Vigenère")

if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
