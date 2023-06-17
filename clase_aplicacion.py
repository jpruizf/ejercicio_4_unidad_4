from tkinter import*
from tkinter import ttk, messagebox
from functools import partial
class Aplicacion():
    __ventana = None
    __global_operation = None
    __numero = None
    __operador = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("200x200")
        self.__ventana.title("Calculadora")
        mainframe = ttk.Frame(self.__ventana,padding="5 5 12 5")
        mainframe.grid(row=0, column=0, sticky=(N,W,E,S))
        mainframe.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)
        mainframe["borderwidth"] = 2
        mainframe["relief"] = 'sunken'
        self.__global_operation = StringVar()
        self.__numero = StringVar()
        self.__operador = StringVar()
        self.__global_operation.trace("w", self.calculo)
        self.__global_operation_entry = ttk.Entry(mainframe, width=7, textvariable= self.__global_operation)
        self.__global_operation_entry.grid(row=0, column=2, sticky=(E))
        ttk.Button(mainframe, text='1', command=partial(self.__numero, '1')).grid(row=1,column=1,sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.__numero,'2')).grid(row=1, column=2, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.__numero,'3')).grid(row=1, column=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.__numero,'4')).grid(row=2, column=1, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.__numero,'5')).grid(row=2, column=2, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.__numero,'6')).grid(row=2, column=3, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.__numero,'7')).grid(row=3, column=1, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.__numero,'8')).grid(row=3, column=2, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.__numero,'9')).grid(row=3, column=3, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.__numero,'0')).grid(row=4, column=1, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.__operador,'+')).grid(row=1, column=4, sticky=E)
        ttk.Button(mainframe, text='-', command=partial(self.__operador,'-')).grid(row=2, column=4, sticky=E)
        ttk.Button(mainframe, text='*', command=partial(self.__operador,'*')).grid(row=3, column=4, sticky=E)
        ttk.Button(mainframe, text='/', command=partial(self.__operador,'/')).grid(row=4, column=4, sticky=E)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=7, pady=7)
        self.__global_operation_entry.focus()
        self.__ventana.mainloop()
    def calculo(self):
        if self.__global_operation_entry.get()!='':
            try:
                total = self.__numero.get()
                self.__global_operation.set(1*total)
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor valido')
                self.__global_operation.set("")
                self.__global_operation_entry.focus()
        else:
            self.__global_operation.set("")
