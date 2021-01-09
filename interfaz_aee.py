import tkinter as tk
import functools
from tkinter import filedialog
from tkinter import *
from affine_vignere import ae,aee,modinv

class VentanaAEE(tk.Toplevel):
    def __init__(self,  parent, vent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("AEE")
        self.geometry("640x480")
        self.configure(bg='NavajoWhite2')
        self.filename = ""
        self.var_inv = 0
        self.var_alpha = IntVar()
        self.var_beta = IntVar()
        self.var_ene = 0
        self.var_gcd = 0
    
        info = tk.Label(self, text="{}".format(vent),font=('Arial',18,'bold italic')
                        ,background='saddle brown', foreground = 'white')
        info.grid(row=0,column=1,padx=20)
        
        lbla = tk.Label(self, text="Primer numero:",font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lbla.grid(row=1,column=0,pady=15)
        
        self.alpha = tk.Entry(self, width = 20,textvariable=self.var_alpha,
                             font=('Arial',12))
        self.alpha.grid(row=1, column=1)
        
        lblb = tk.Label(self, text="Segundo numero:",font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lblb.grid(row=2,column=0)
        
        self.beta = tk.Entry(self, width = 20,textvariable=self.var_beta,
                             font=('Arial',12))
        self.beta.grid(row=2, column=1)
        
        lblc = tk.Label(self, text="Máximo común divisor:",
                        font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lblc.grid(row=4,column=0,padx=20,pady=20)
        self.gcd = tk.Entry(self, width = 10,state='disabled',
                             font=('Arial',12))
        self.gcd.grid(row=4, column=1)
        
        lbld = tk.Label(self, text="Puede expresarse como:",
                        font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lbld.grid(row=5,column=0,padx=20)
        self.expr = tk.Entry(self, width = 30,state='disabled',
                             font=('Arial',12))
        self.expr.grid(row=5, column=1)
        
        lble = tk.Label(self, text="El inverso de",
                        font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lble.grid(row=6,column=0,padx=20,pady=20)
        self.alf = tk.Entry(self, width = 10,state='disabled',
                             font=('Arial',12))
        self.alf.grid(row=6, column=1)
        
        lblf = tk.Label(self, text="modulo",
                        font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lblf.grid(row=7,column=0,padx=20)
        self.mod = tk.Entry(self, width = 10,state='disabled',
                             font=('Arial',12))
        self.mod.grid(row=7, column=1)
        
        lblg = tk.Label(self, text="es",
                        font=('Arial',12,'bold italic')
                        ,background='NavajoWhite2', foreground = 'grey1')
        lblg.grid(row=8,column=0,padx=20, pady=20)
        self.inv = tk.Entry(self, width = 10,state='disabled',
                             font=('Arial',12))
        self.inv.grid(row=8, column=1)

        
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular,
                               bg='saddle brown',width=10,height = 1,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_calcular.grid(row=3,column=0,pady=10)
        
        btn_borrar = tk.Button(self, text="Borrar", command=self.borrar,
                               bg='saddle brown',width=10,height = 1,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_borrar.grid(row=3,column=1,pady=10)
        

        
        
        self.protocol("WM_DELETE_WINDOW", self.volver)
        btn_volver = tk.Button(self, text="Volver", command=self.volver,
                               bg='saddle brown',width=10,height = 2,
                               foreground='white',font=('Arial',10,'bold italic'))

        btn_volver.grid(row=0,column=0)
    
        parent.withdraw()

    def volver(self):
        self.parent.deiconify()
        self.destroy()
        
    def calcular(self):
        a= self.var_alpha.get()
        b= self.var_beta.get()
        mcd,x,y= aee(a,b)
        expresion = "{}*({})+{}*({})={}".format(a, x, b, y, mcd)
        self.gcd.configure(state="normal")
        self.gcd.delete(0,'end')
        self.gcd.insert(END,mcd)
        self.gcd.configure(state="disable")
        self.expr.configure(state="normal")
        self.expr.delete(0,'end')
        self.expr.insert(END,expresion)
        self.expr.configure(state="disable")
        self.alf.configure(state="normal")
        self.alf.delete(0,'end')
        self.alf.insert(END, a)
        self.alf.configure(state="disable")
        self.mod.configure(state="normal")
        self.mod.delete(0,'end')
        self.mod.insert(END,b)
        self.mod.configure(state="disable")
        self.inv.configure(state="normal")
        self.inv.delete(0,'end')
        if(mcd != 1):
            self.inv.insert(END,"No Existe")
        else: self.inv.insert(END,modinv(a,b))
        self.inv.configure(state="disable")
    
    def borrar(self):
        self.alpha.delete(0,'end')
        self.beta.delete(0,'end')
        self.gcd.configure(state="normal")
        self.gcd.delete(0,'end')
        self.gcd.configure(state="disable")
        self.expr.configure(state="normal")
        self.expr.delete(0,'end')
        self.expr.configure(state="disable")
        self.alf.configure(state="normal")
        self.alf.delete(0,'end')
        self.alf.configure(state="disable")
        self.mod.configure(state="normal")
        self.mod.delete(0,'end')
        self.mod.configure(state="disable")
        self.inv.configure(state="normal")
        self.inv.delete(0,'end')
        self.inv.configure(state="disable")