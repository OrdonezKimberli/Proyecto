import tkinter as tk
from tkinter import messagebox, ttk
import csv
from datetime import datetime
import os

ARCHIVO_ASISTENCIA = 'asistencias.csv'

if not os.path.exists(ARCHIVO_ASISTENCIA):
    with open(ARCHIVO_ASISTENCIA, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Nombre', 'DNI', 'Accion', 'Fecha', 'Hora'])

def registrar_asistencia(accion):
    nombre = entry_nombre.get()
    dni = entry_dni.get()
    if not nombre or not dni:
        messagebox.showwarning("Campos Vacíos", "Por favor ingrese nombre y DNI.")
        return

    ahora = datetime.now()
    fecha = ahora.strftime('%Y-%m-%d')
    hora = ahora.strftime('%H:%M:%S')

    with open(ARCHIVO_ASISTENCIA, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nombre, dni, accion, fecha, hora])

    messagebox.showinfo("Registro Exitoso", f"{accion} registrada para {nombre} a las {hora}")
    entry_nombre.delete(0, tk.END)
    entry_dni.delete(0, tk.END)
    actualizar_historial()

def actualizar_historial():
    for row in tree.get_children():
        tree.delete(row)

    with open(ARCHIVO_ASISTENCIA, 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            tree.insert("", tk.END, values=row)

ventana = tk.Tk()
ventana.title("Control de Asistencias - Hospital")
ventana.geometry("700x500")

frame_formulario = tk.Frame(ventana)
frame_formulario.pack(pady=10)

tk.Label(frame_formulario, text="Nombre del Trabajador:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_formulario, width=30)
entry_nombre.grid(row=0, column=1, padx=5)

tk.Label(frame_formulario, text="DNI:").grid(row=1, column=0, padx=5, pady=5)
entry_dni = tk.Entry(frame_formulario, width=30)
entry_dni.grid(row=1, column=1, padx=5)

btn_entrada = tk.Button(frame_formulario, text="Registrar Entrada", command=lambda: registrar_asistencia("Entrada"))
btn_entrada.grid(row=2, column=0, pady=10)

btn_salida = tk.Button(frame_formulario, text="Registrar Salida", command=lambda: registrar_asistencia("Salida"))
btn_salida.grid(row=2, column=1, pady=10)

frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=10)

tree = ttk.Treeview(frame_tabla, columns=('Nombre', 'DNI', 'Accion', 'Fecha', 'Hora'), show='headings')
for col in tree['columns']:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack()

actualizar_historial()
ventana.mainloop()
