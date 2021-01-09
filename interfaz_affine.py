import tkinter as tk
import functools
from tkinter import filedialog
from tkinter import *
from affine_vignere import get_text_string, ae, factores, cifrado_affine, descifrar_affine, save_text

class VentanaAffine(tk.Toplevel):
    def __init__(self,  parent, vent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Cifrado Affine")
        self.geometry("640x480")
        self.configure(bg='NavajoWhite2')
        self.filename = ""
        self.textoc=""
        self.var_texto = ""
        self.var_alpha = IntVar()
        self.var_beta = IntVar()
        self.var_ene = IntVar()
    
        info = tk.Label(self, text="{}".format(vent),font=('Arial',20,'bold italic')
                        ,background='saddle brown', foreground = 'white')
        info.grid(row=0,column=1,padx=20)
        
        lbl = tk.Label(self, text="Ruta de archivo:",font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lbl.grid(row=1,column=0)
        
        self.bar = tk.Entry(self, width = 40,state='disabled')
        self.bar.grid(row=1, column=1,pady=30)
        
        btn_ex = tk.Button(self,text="Examinar",font=('Helvetica',10),
                           bg="saddle brown",command=self.abrir,
                           foreground='white',width=10)
        btn_ex.grid(row = 1,column=2,padx="15")
        
        lbla = tk.Label(self, text="Introduzca Alpha:",font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lbla.grid(row=2,column=0,pady=15)
        
        self.alpha = tk.Entry(self, width = 20,textvariable=self.var_alpha,
                             font=('Arial',12))
        self.alpha.grid(row=2, column=1)
        
        lblb = tk.Label(self, text="Introduzca Beta:",font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lblb.grid(row=3,column=0)
        
        self.beta = tk.Entry(self, width = 20,textvariable=self.var_beta,
                             font=('Arial',12))
        self.beta.grid(row=3, column=1)
        
        lblc = tk.Label(self, text="Introduzca el tamaño\ndel abecedario:",
                        font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lblc.grid(row=4,column=0,pady=15,padx=10)
        
        self.ene = tk.Entry(self, width = 20,textvariable=self.var_ene,
                             font=('Arial',12))
        self.ene.grid(row=4, column=1)
        
        btn_cifrar = tk.Button(self, text="Cifrar", command=self.cifrar,
                               bg='saddle brown',width=10,height = 2,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_cifrar.grid(row=5, column=0)
        
        btn_descifrar = tk.Button(self, text="Descifrar", command=self.descifrar,
                               bg='saddle brown',width=10,height = 2,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_descifrar.grid(row=5,column=1)
        
        btn_borrar = tk.Button(self,text="Borrar",font=('Helvetica',10),
                           bg="saddle brown",command=self.borrar,
                           foreground='white',height=2,width=10)
        btn_borrar.grid(row=5,column=2)
        
        self.muestra = tk.Text(self, width = 60, height = 8, state='disable')
        self.muestra.grid(row=6,column=0, columnspan=2,pady=15,padx=15)
        
        btn_guardar = tk.Button(self,text="Guardar",font=('Helvetica',10),
                           bg="saddle brown",command=self.guardar,
                           foreground='white',width=10,height=2)
        btn_guardar.grid(row=6,column=2)
        
        self.protocol("WM_DELETE_WINDOW", self.volver)
        btn_volver = tk.Button(self, text="Volver", command=self.volver,
                               bg='saddle brown',width=10,height = 2,
                               foreground='white',font=('Arial',10,'bold italic'))

        btn_volver.grid(row=0,column=0)
    
        parent.withdraw()

    def volver(self):
        self.parent.deiconify()
        self.destroy()
        
    def abrir(self):
       self.filename = filedialog.askopenfilename(initialdir = "C:/",
                                             title="Seleccionar archivo",
                                  filetypes=(("Txt",".txt"),("Affine",".aff"),
                                             ("Vignere",".vig")))
       self.var_texto = get_text_string(self.filename)
       self.bar.configure(state='normal')
       self.bar.insert(END,self.filename)
       self.bar.configure(state='disabled')
       
    def borrar(self):
        self.var_texto = ""
        self.filename = ""
        self.alpha.delete(0,'end')
        self.beta.delete(0,'end')
        self.ene.delete(0,'end')
        self.bar.configure(state="normal")
        self.bar.delete(0,'end')
        self.bar.configure(state="disable")
        self.muestra.configure(state="normal")
        self.muestra.delete('1.0',END)
        self.muestra.configure(state="disable")
        
    def cifrar(self):
        a = self.var_alpha.get()
        b = self.var_beta.get()
        n = self.var_ene.get()
        posibles = ' '.join([str(elem) for elem in factores(1,n)[:15]])
        if(ae(a,n)!=1):
            messagebox.showinfo('Numeros no coprimos', 'Los valores de alfa'
                                +' y del tamaño del abecedario'
                                +'no son coprimos\nIngrese otros valores'
                                +'\nAlgunos valores de alfa posibles son:'
                                +posibles)
            return
        self.textoc = cifrado_affine(self.var_texto,a,b,n)
        self.muestra.configure(state="normal")
        self.muestra.insert(END, self.textoc)
        self.muestra.configure(state="disable")
        
    def descifrar(self):
        a = self.var_alpha.get()
        b = self.var_beta.get()
        n = self.var_ene.get()
        posibles = ' '.join([str(elem) for elem in factores(1,n)[:15]])
        if(ae(a,n)!=1):
            messagebox.showinfo('Numeros no coprimos', 'Los valores de alfa'
                                +' y del tamaño del abecedario'
                                +'no son coprimos\nIngrese otros valores'
                                +'\nAlgunos valores de alfa posibles son:'
                                +posibles)
            return
        self.textoc = descifrar_affine(self.var_texto,a,b,n)
        self.muestra.configure(state="normal")
        self.muestra.insert(END, self.textoc)
        self.muestra.configure(state="disable")
        
    def guardar(self):
        fileas = filedialog.asksaveasfilename(initialdir = "C:/",
                                             title="Seleccionar archivo",
                                             defaultextension=".aff",
                                  filetypes=(("Affine",".aff"),("Txt",".txt"),
                                             ("Vignere",".vig")))
        save_text(self.textoc, fileas)
        
        