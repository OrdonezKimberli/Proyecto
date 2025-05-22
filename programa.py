import tkinter as tk
from tkinter import messagebox
asistencia = []
def registrar_asistencia():
    nombre = entry_nombre.get().strip()
    estado = var_asistencia.get()

    if not nombre:
        messagebox.showwarning("Advertencia", "Por favor, ingresa el nombre del empleado.")
        return

