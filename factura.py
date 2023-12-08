from tkinter import Tk, Label, Entry, Button, messagebox
from fpdf import FPDF

class facturaInit:
    def __init__(self, root):
        self.root = root
        self.root.title("Facturas")

        self.business = Entry(root)
        self.ruc = Entry(root)
        self.social = Entry(root)
        self.address = Entry(root)
        self.product_name = Entry(root)
        self.product_price = Entry(root)
        self.quantity = Entry(root)
        
        self.products = []
        self.add_product_entry()

        Label(root, text="Empresa: ").grid(row=0, column=0)
        self.business.grid(row=0, column=1)

        Label(root, text="RUC: ").grid(row=2, column=0)
        self.ruc.grid(row=2, column=1)

        Label(root, text="Razon Social: ").grid(row=5, column=0)
        self.social.grid(row=5, column=1)

        Label(root, text="Direccion: ").grid(row=1, column=0)
        self.address.grid(row=1, column=1)


        

        Button(root, text="Agregar producto", command=self.add_product_entry).grid(row=1, column=2)
        Button(root, text="Imprimir factura", command = self.gnt_fta).grid(row=0, column=2)

        
    def add_product_entry(self):
        row = len(self.products) + 6  # Determinar la fila para el nuevo producto
        product_label = Label(self.root, text=f"Producto {len(self.products) + 1}: ")
        product_label.grid(row=row, column=0)
        product_entry = Entry(self.root)
        product_entry.grid(row=row, column=1)
        price_label = Label(self.root, text=f"Precio {len(self.products) + 1}: ")
        price_label.grid(row=row, column=2)
        price_entry = Entry(self.root)
        price_entry.grid(row=row, column=3)
        quantity_label = Label(self.root, text=f"Cantidad {len(self.products) + 1}: ")
        quantity_label.grid(row=row, column=4)
        quantity_entry = Entry(self.root)
        quantity_entry.grid(row=row, column=5)
        self.products.append((product_entry, price_entry, quantity_entry)) 

    def gnt_fta(self):
        business = self.business.get()
        ruc = self.ruc.get()
        social = self.social.get()
        address = self.address.get()
       
        

        if not all((business, ruc, social, address)):
            messagebox.showerror("Error", "Por favor, rellene los campos")
            return
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.image('./images/factura.jpg', x=0, y=0, w=210)

        current_y = 100
        

        pdf.set_xy(24, 34.5)
        pdf.cell(0, 10, f"{business}", 0, 1)

        pdf.set_xy(15, 43)
        pdf.cell(0, 10, f"{ruc}", 0, 1)

        pdf.set_xy(32, 51.5)
        pdf.cell(0, 10, f"{social}", 0, 1)

        pdf.set_xy(29, 60)
        pdf.cell(0, 10, f"{address}", 0, 1)

        total_amount = 0
        for i, (product_entry, price_entry, quantity_entry) in enumerate(self.products, start = 1):
            product = product_entry.get()
            price = price_entry.get()
            quantity = quantity_entry.get()
            if not all ((product, price, quantity)):
                messagebox.showerror("Error", f"Falta informacion para el producto {i}")
                return
            try:
                price = float(price)
                quantity = int(quantity)
            except ValueError:
                messagebox.showerror("Error", f"El precio y la cantidad deben ser numeros valido para el producto {i}")
                return
            total_product = price * quantity
            total_amount += total_product

            pdf.set_xy(10, current_y)
            pdf.cell(20,0, f"{i}: {product}", 0, 1)

            pdf.set_xy(70, current_y) 
            pdf.cell(30, 0, f"{price}", 0, 1)

            pdf.set_xy(120, current_y) 
            pdf.cell(40, 0, f"{quantity}", 0, 1)

            pdf.set_xy(160, current_y) 
            pdf.cell(50, 0, f"{total_product}", 0, 1)
            current_y += 5

        total_iva = (total_amount * 18) / 100
        total_amount += round(total_iva)


    


        pdf.set_xy(170, 180)
        pdf.cell(0, 10, f"{total_iva} ", 0, 1 )

        pdf.set_xy(170, 210)
        pdf.cell(0, 10, f"{total_amount}", 0, 1)
        

        pdf_output = f"{business}_factura.pdf"
        pdf.output(pdf_output)

        messagebox.showinfo("Factura generada", f"se ha generado la factura como {pdf_output}")

if __name__ == "__main__":
    root = Tk()
    app = facturaInit(root)
    root.mainloop()

