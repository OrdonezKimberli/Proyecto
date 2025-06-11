import tkinter as tk
from tkinter import ttk, messagebox

class Trabajador:
    def __init__(self, nombre, edad, area, id_, asistencia, entrada, salida, vacaciones):
        self.nombre = nombre
        self.edad = edad
        self.area = area
        self.id = id_
        self.asistencia = asistencia
        self.entrada = entrada
        self.salida = salida
        self.vacaciones = vacaciones

    def to_tuple(self):
        return (self.id, self.nombre, self.edad, self.area,
                self.asistencia, self.entrada, self.salida, self.vacaciones)

class AppRegistro:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Trabajadores con Vacaciones")
        self.root.configure(bg="#7763CE")

        self.trabajadores = []

        
        self.campos = ["Nombre", "Edad", "Área de Trabajo", "ID", "Hora de Entrada", "Hora de Salida"]
        self.entradas = {}
        for i, campo in enumerate(self.campos):
            tk.Label(root, text=campo + ":", bg="#7763CE").grid(row=i, column=0, sticky="e", pady=3, padx=5)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1, pady=3, padx=5)
            self.entradas[campo] = entry

        tk.Label(root, text="¿Asistió hoy?", bg="#7763CE").grid(row=6, column=0, sticky="e")
        self.asistencia_var = tk.StringVar(value="Sí")
        ttk.Combobox(root, textvariable=self.asistencia_var, values=["Sí", "No"], state="readonly").grid(row=6, column=1)

        tk.Label(root, text="Periodo de Vacaciones:", bg="#7763CE").grid(row=7, column=0, columnspan=2, pady=5)
        self.periodo_var = tk.StringVar()
        self.periodos = ["enero-febrero", "marzo-abril", "mayo-junio", "julio-agosto"]
        self.periodo_menu = ttk.Combobox(root, textvariable=self.periodo_var, values=self.periodos, state="readonly")
        self.periodo_menu.grid(row=8, column=0, columnspan=2)

        tk.Button(root, text="Guardar Trabajador", command=self.guardar_trabajador).grid(row=9, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Mostrar Historial", command=self.mostrar_historial).grid(row=10, column=0, columnspan=2)

        columnas = ("ID", "Nombre", "Edad", "Área", "Asistencia", "Entrada", "Salida", "Vacaciones")
        self.tree = ttk.Treeview(root, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.grid(row=11, column=0, columnspan=2, pady=10)

        self.periodos_tomados = set()

    def guardar_trabajador(self):
        
        datos = {}
        for campo, entry in self.entradas.items():
            valor = entry.get().strip()
            if not valor:
                messagebox.showerror("Error", f"Falta completar el campo: {campo}")
                return
            datos[campo] = valor

        if not datos["Edad"].isdigit():
            messagebox.showerror("Error", "La edad debe ser un número.")
            return

        id_ = datos["ID"]
        if any(t.id == id_ for t in self.trabajadores):
            messagebox.showerror("Error", "ID duplicado. Cada trabajador debe tener un ID único.")
            return

        
        periodo = self.periodo_var.get()
        if not periodo:
            messagebox.showerror("Error", "Debe seleccionar un periodo vacacional.")
            return
        if periodo in self.periodos_tomados:
            messagebox.showerror("Error", f"El {periodo} ya fue elegido por otro trabajador.")
            return

        self.periodos_tomados.add(periodo)

        
        trabajador = Trabajador(
            nombre=datos["Nombre"],
            edad=datos["Edad"],
            area=datos["Área de Trabajo"],
            id_=id_,
            asistencia=self.asistencia_var.get(),
            entrada=datos["Hora de Entrada"],
            salida=datos["Hora de Salida"],
            vacaciones=periodo
        )
        self.trabajadores.append(trabajador)

        
        for entry in self.entradas.values():
            entry.delete(0, tk.END)
        self.asistencia_var.set("Sí")
        self.periodo_var.set("")

        messagebox.showinfo("Guardado", f"Trabajador {trabajador.nombre} registrado correctamente.")

    def mostrar_historial(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        trabajadores_ordenados = sorted(self.trabajadores, key=lambda t: t.id)
        for t in trabajadores_ordenados:
            self.tree.insert("", tk.END, values=t.to_tuple())

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AppRegistro(ventana)
    ventana.mainloop()
