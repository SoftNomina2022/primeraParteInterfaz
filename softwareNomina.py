from tkinter import *
from tkinter import messagebox
class Bill_App():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#fafafa")
        self.root.title("Calculadora pago de nómina")
        title = Label(self.root, text="Sistema de pago de Nómina", bd=12, relief=RIDGE, font=(
            "Arial Black", 20), bg="#1e3c68", fg="white").pack(fill=X)
        # ===================================variables=======================================================================================
        self.diasLaborales = IntVar() #Dias que laboró el empleado durante el mes
        self.salarioDia = IntVar() #Calcular el día
       
        self.canthrn = IntVar()  #Cantidad de horas con recargo nocturno
        self.canthed = IntVar()  #Cantidad de horas extras diurnas
        self.canthen = IntVar()  #Cantidad de horas extras nocturnas
        self.canthrfd = IntVar() #Cantidad de horas con recargo festivo diurno
        self.canthrfn = IntVar() #Cantidad de horas con recargo festivo nocturno
        self.canthdfe = IntVar() #Cantidad de horas diurnas festivas extras
        self.canthnfe = IntVar() #Cantidad de horas nocturnas festivas extras
       
        self.c_name = StringVar() #Nombre del empleado
 
        self.salario = IntVar()     #Salario mensual
        self.dias = StringVar()     #Reset dias laborales
        self.setsd = StringVar()    #Envio salario diario
        self.setsb = StringVar()    #Envio salario basico
        self.sethl = StringVar()    #Envio hora laboral
        self.setatd = StringVar()   #Envio auxilio de transporte diario
        self.setatp = StringVar()   #Envio auxilio de transporte a pagar
        self.settsba = StringVar()  #Envio total salario basico + auxilio de transporte
        self.setther = StringVar()  #Envio total horas extras y recargos
        self.settap = StringVar()   #Envio total a pagar
        # ==========================================Detalles del Empleado=================================================
        details = LabelFrame(self.root, text="Detalles del Empleado", font=(
            "Arial Black", 12), bg="#3891c8", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="Nombre del Empleado", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=0, padx=15)
 
        cust_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.c_name).grid(row=0, column=1, padx=8)
 
        contact_name = Label(details, text="Salario básico mensual", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=2, padx=10)
 
        contact_entry = Entry(details, borderwidth=4, width=30,
                              textvariable=self.salario).grid(row=0, column=3, padx=8)
       
 
        bill_name = Label(details, text="No de pago", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=4, padx=10)
 
        bill_entry = Entry(details, borderwidth=4, width=30).grid(row=0, column=5, padx=8)
        # =======================================Calculo x Día=================================================================
        snacks = LabelFrame(self.root, text="Calculo x Día", font=(
            "Arial Black", 12), bg="#3891c8", fg="#ffffff", relief=GROOVE, bd=10)
        snacks.place(x=5, y=180, height=380, width=325)
 
        item1 = Label(snacks, text="Dias laborados", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item1_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.diasLaborales).grid(row=0, column=1, padx=10)
 
        item2 = Label(snacks, text="Valor día laboral", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item2_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.setsd).grid(row=1, column=1, padx=10)
 
        item3 = Label(snacks, text="Valor Hora laboral", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item3_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.sethl).grid(row=2, column=1, padx=10)
 
        item4 = Label(snacks, text="Valor del día", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
 
        item5 = Label(snacks, text="Auxilio de transporte", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item5_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.setatd).grid(row=4, column=1, padx=10)
 
        item6 = Label(snacks, text="Valor a pagar", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
       
 
        item7 = Label(snacks, text="Auxilio de transporte", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item7_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.setatp).grid(row=6, column=1, padx=10)
        # ===================================Horas Extras y Recargos Columna 1=====================================================================================
        grocery = LabelFrame(self.root, text="Horas Extras y Recargos", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="#ffffff")
        grocery.place(x=340, y=180, height=380, width=325)
 
        item8 = Label(grocery, text="Hora Extra Diurna", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item8_entry = Entry(grocery, borderwidth=2, width=15,
                            textvariable=self.canthed).grid(row=1, column=1, padx=10)
       
        item9 = Label(grocery, text="Hora con recargo", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item10 = Label(grocery, text="festivo diurno", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item10_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.canthrfd).grid(row=3, column=1, padx=10)
 
        item11 = Label(grocery, text="Hora con recargo", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item12 = Label(grocery, text="festivo nocturno", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
        item12_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.canthrfn).grid(row=5, column=1, padx=10)
 
        item13 = Label(grocery, text="Hora Diurna ", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item14 = Label(grocery, text="Festiva Extra", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=7, column=0, pady=11)
        item14_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.canthdfe).grid(row=7, column=1, padx=10)
        # ========================================Horas Extras y Recargos Columna 2===============================================================================
        hygine = LabelFrame(self.root, text="Horas Extras y Recargos", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="#ffffff")
        hygine.place(x=677, y=180, height=380, width=325)
 
        item15 = Label(hygine, text="Hora con Recargo", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item16 = Label(hygine, text="Nocturno Ordinario", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item16_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.canthrn).grid(row=1, column=1, padx=10)
 
        item18 = Label(hygine, text="Hora Extra Nocturna", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item18_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.canthen).grid(row=3, column=1, padx=10)
 
 
        item20 = Label(hygine, text="Hora Nocturna", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
     
 
        item21 = Label(hygine, text="Festiva Extra", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item21_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.canthnfe).grid(row=6, column=1, padx=10)
        # =====================================================Área de Impresión==============================================================================
        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#3891c8")
        billarea.place(x=1010, y=188, width=330, height=372)
 
        bill_title = Label(billarea, text="Área de Impresión", font=(
            "Arial Black", 17), bd=7, relief=GROOVE, bg="#3891c8", fg="#ffffff").pack(fill=X)
 
        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # =================================================Resumen de pago de nómina=========================================================================================
        billing_menu = LabelFrame(self.root, text="Resumen de pago de nómina", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)
 
        total_snacks = Label(billing_menu, text="Salario devengado", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=0, column=0)
        total_snacks_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.setsb).grid(row=0, column=1, padx=10, pady=7)
 
        total_grocery = Label(billing_menu, text="Aux. transporte", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=1, column=0)
        total_grocery_entry = Entry(billing_menu, width=30, borderwidth=2,
                                    textvariable=self.setatp).grid(row=1, column=1, padx=10, pady=7)
 
        total_hygine = Label(billing_menu, text="Total Salario + Aux.", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=2, column=0)
        total_hygine_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.settsba).grid(row=2, column=1, padx=10, pady=7)
 
        tax_snacks = Label(billing_menu, text="Total HE y Recargos", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=0, column=2)
        tax_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.setther).grid(
            row=0, column=3, padx=10, pady=7)
 
        tax_hygine = Label(billing_menu, text="Total a pagar", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=2, column=2)
        tax_hygine_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.settap).grid(
            row=2, column=3, padx=10, pady=7)
 
        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#fafafa")
        button_frame.place(x=830, width=500, height=95)
 
        button_total = Button(button_frame, text="Calcular Pago", font=("Arial Black", 15), pady=10,
                              bg="#3891c8", fg="#ffffff").grid(row=0, column=0, padx=12)
        button_clear = Button(button_frame, text="Resetear", font=("Arial Black", 15), pady=10,
                              bg="#3891c8", fg="#ffffff").grid(row=0, column=1, padx=10, pady=6)
        button_exit = Button(button_frame, text="Imprimir", font=("Arial Black", 15), pady=10, bg="#3891c8",
                             fg="#ffffff", width=8).grid(row=0, column=2, padx=10, pady=6)
root = Tk()
obj = Bill_App(root)
root.mainloop()
