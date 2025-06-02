import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def registrar_entrada():
    nombre = entry_nombre.get()
    if not nombre:
        messagebox.showwarning("Entrada inválida", "Por favor, ingresa tu nombre.")
        return

    turno = var_turno.get()
    if turno == "Seleccionar turno":
        messagebox.showwarning("Turno inválido", "Por favor, selecciona un turno.")
        return

    hora_actual = datetime.now()
    hora_turno = {
        "Matutino": datetime.strptime("08:00", "%H:%M"),
        "Vespertino": datetime.strptime("16:00", "%H:%M"),
        "Nocturno": datetime.strptime("00:00", "%H:%M")
    }.get(turno)

    if hora_turno:
        if hora_actual > hora_turno + timedelta(minutes=10):
            mensaje = f"¡Retardo! Llegaste {hora_actual - (hora_turno + timedelta(minutes=10))} tarde."
        else:
            mensaje = f"Entrada registrada a las {hora_actual.strftime('%H:%M:%S')}."
    else:
        mensaje = "Turno no válido."

    messagebox.showinfo("Registro de entrada", mensaje)

ventana = tk.Tk()
ventana.title("Control de Asistencias")
ventana.geometry("300x250")

tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

tk.Label(ventana, text="Selecciona tu turno:").pack(pady=5)
var_turno = tk.StringVar(value="Seleccionar turno")
turnos = ["Matutino", "Vespertino", "Nocturno"]
turno_menu = tk.OptionMenu(ventana, var_turno, *turnos)
turno_menu.pack(pady=5)

btn_registrar = tk.Button(ventana, text="Registrar Entrada", command=registrar_entrada)
btn_registrar.pack(pady=20)

ventana.mainloop()
