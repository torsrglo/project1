import tkinter as tk



class CountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Account")

        self.income = []
        self.bill = []

        tk.Label(self.root, text="Ingreso: ", background="grey").pack()
        self.enter_incomes = tk.Entry(self.root, bg="grey")
        self.enter_incomes.pack()

        self.btn_income = tk.Button(self.root, text="Registrar ingreso: ", command=self.register_income, bg="grey")
        self.btn_income.pack()


        tk.Label(self.root, text="Gasto: ", background="grey").pack()
        self.enter_bill = tk.Entry(self.root, bg="grey")
        self.enter_bill.pack()

        self.btn_bill = tk.Button(self.root, text="Registrar gasto: ", command=self.register_bill, bg="grey")
        self.btn_bill.pack()

        self.btn_report = tk.Button(self.root, text="Generar informe: ", command=self.generate_report, bg="grey")
        self.btn_report.pack()

        self.enter_incomes.config(validate="key",validatecommand=(self.root.register(self.validate_input), "%P"))
        self.enter_bill.config(validate="key",validatecommand=(self.root.register(self.validate_input), "%P"))
    def validate_input(self, P):
        return all(char.isdigit() or (char == '.' and P.count('.') < 2) for char in P) or P == ""

    def on_validate(self, new_value):
        return new_value.isdigit() or new_value == ""

    def register_income(self):
        quantity = float(self.enter_incomes.get())
        self.income.append(quantity)
        self.enter_incomes.delete(0, tk.END)
        
    def register_bill(self):
        quantity = float(self.enter_bill.get())
        self.bill.append(quantity)
        self.enter_bill.delete(0, tk.END)

    def generate_report(self):
        total_income = sum(self.income)
        total_bill = sum (self.bill)
        balance = total_income - total_bill

        report = f"Ingresos totales : {total_income}\nGastos totales: {total_bill}\nBalance: {balance}" 

        window_report = tk.Toplevel(self.root)
        tk.Label(window_report, text=report).pack()
   



if __name__ == "__main__":
    root = tk.Tk()
    app = CountApp(root)
    root.config(bg="grey")
    root.mainloop()
            


