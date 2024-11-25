
# Author : Luis Chero


from tkinter import *
from tkinter import ttk
from fuentes import *

win = Tk()
win.geometry("500x500+700+180")
win.title("Luis")

contactos_id = 0  

def agregar_contacto():
    global contactos_id
    nombre = input_nombre.get().strip()
    numero = input_numero.get().strip()

    if nombre and numero:
        contactos_id += 1
        tabla.insert("", "end", values=(contactos_id, nombre, numero)) 
        input_nombre.delete(0, END)  
        input_numero.delete(0, END)
        input_numero.insert(0, "+51 ") 

def guardar_contactos():
    with open("contactos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("ID\tNombre\tNúmero\n")  
        for row in tabla.get_children():
            valores = tabla.item(row)["values"]
            archivo.write(f"{valores[0]}\t{valores[1]}\t{valores[2]}\n")  
    print("Contactos guardados en 'contactos.txt'")

frame_header = Frame(win, bg="#e6b9d4", pady=20)
frame_header.pack(fill="x")

label_header = Label(frame_header, text="AGREGAR CONTACTOS:", font=fuente_titulo, bg="#e6b9d4", fg="#333")
label_header.pack()

frame_body = Frame(win, bg="#f0c1e1", padx=10, pady=10)
frame_body.pack(pady=10)

label_nombre = Label(frame_body, text="Nombre:", font=fuente_labels, bg="#f0c1e1", anchor="w")
label_nombre.grid(row=0, column=0, sticky="w", pady=10)

input_nombre = Entry(frame_body, font=fuente_inputs, width=30, relief="flat", highlightthickness=2, highlightbackground="#ccc", highlightcolor="#333")
input_nombre.grid(row=0, column=1, pady=10)

label_numero = Label(frame_body, text="Número:", font=fuente_labels, bg="#f0c1e1", anchor="w")
label_numero.grid(row=1, column=0, sticky="w", pady=10)

input_numero = Entry(frame_body, font=fuente_inputs, width=30, relief="flat", highlightthickness=2, highlightbackground="#ccc", highlightcolor="#333")
input_numero.insert(0, "+51 ")
input_numero.grid(row=1, column=1, pady=10)

btn_agregar = Button(frame_body, text="Añadir", font=("Arial", 12), command=agregar_contacto, bg="#fff", fg="#333", relief="flat", width=15)
btn_agregar.grid(row=2, column=0, columnspan=2, pady=20)


btn_guardar = Button(frame_body, text="Guardar Contactos", font=("Arial", 12), command=guardar_contactos, bg="#fff", fg="#333", relief="flat", width=15)
btn_guardar.grid(row=3, column=0, columnspan=2, pady=20)

frame_table = Frame(win, bg="#f0c1e1", padx=20, pady=10)
frame_table.pack(fill="both", expand=True)

scrollbar_y = Scrollbar(frame_table, orient="vertical")
scrollbar_y.pack(side=RIGHT, fill=Y)

tabla = ttk.Treeview(frame_table, columns=("ID", "Nombre", "Número"), show="headings", yscrollcommand=scrollbar_y.set, height=10)
tabla.pack(fill="both", expand=True)
scrollbar_y.config(command=tabla.yview)

tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Número", text="Número")

tabla.column("ID", anchor="center", width=50)
tabla.column("Nombre", anchor="center", width=200)
tabla.column("Número", anchor="center", width=150)

win.mainloop()
