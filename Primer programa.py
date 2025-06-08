import tkinter as tk
from tkinter import messagebox
class Trabajador:
    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="Datos del Trabajador", padx=10, pady=10, bg="light blue")
        self.frame.pack(padx=10, pady=5, fill="x")

        self.trabajadores = ["Natalia", "Roberto", "Nahomí", "Victor", "Sonia"]
        self.nombre_var = tk.StringVar(value=self.trabajadores[0])
        self.edad_var = tk.StringVar()
        self.genero_var = tk.StringVar()
        self.area_var = tk.StringVar()
        self.curp_var = tk.StringVar()
        self.nss_var = tk.StringVar()
        self.control_var = tk.StringVar()
        self.telefono_var = tk.StringVar()

        campos = [
            ("Nombre:", tk.OptionMenu(self.frame, self.nombre_var, *self.trabajadores)),
            ("Edad:", tk.Entry(self.frame, textvariable=self.edad_var)),
            ("Género:", tk.Entry(self.frame, textvariable=self.genero_var)),
            ("Área de trabajo:", tk.Entry(self.frame, textvariable=self.area_var)),
            ("CURP:", tk.Entry(self.frame, textvariable=self.curp_var)),
            ("NSS:", tk.Entry(self.frame, textvariable=self.nss_var)),
            ("Núm. de Control:", tk.Entry(self.frame, textvariable=self.control_var)),
            ("Teléfono:", tk.Entry(self.frame, textvariable=self.telefono_var)),
        ]

        for i, (label, widget) in enumerate(campos):
            tk.Label(self.frame, text=label, bg="light blue").grid(row=i, column=0, sticky="w")
            widget.grid(row=i, column=1, sticky="ew")

    def obtener_datos(self):
        return {
            "nombre": self.nombre_var.get(),
            "edad": self.edad_var.get(),
            "genero": self.genero_var.get(),
            "area": self.area_var.get(),
            "curp": self.curp_var.get(),
            "nss": self.nss_var.get(),
            "control": self.control_var.get(),
            "telefono": self.telefono_var.get()
        }

    def limpiar(self):
        self.edad_var.set("")
        self.genero_var.set("")
        self.area_var.set("")
        self.curp_var.set("")
        self.nss_var.set("")
        self.control_var.set("")
        self.telefono_var.set("")

class Jornada:
    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="Datos de la Jornada", padx=10, pady=10, bg="light blue")
        self.frame.pack(padx=10, pady=5, fill="x")

        self.dia_var = tk.StringVar()
        self.entrada_var = tk.StringVar()
        self.salida_var = tk.StringVar()
        self.retardos_var = tk.StringVar()
        self.asistencia_var = tk.StringVar()
        self.faltas_var = tk.StringVar()
        self.turno_var = tk.StringVar()

        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        turnos = ["Matutino", "Vespertino", "Nocturno"]

        campos = [
            ("Día:", tk.OptionMenu(self.frame, self.dia_var, *dias)),
            ("Hora de entrada:", tk.Entry(self.frame, textvariable=self.entrada_var)),
            ("Hora de salida:", tk.Entry(self.frame, textvariable=self.salida_var)),
            ("Retardos:", tk.Entry(self.frame, textvariable=self.retardos_var)),
            ("Asistencia (sí/no):", tk.Entry(self.frame, textvariable=self.asistencia_var)),
            ("Faltas:", tk.Entry(self.frame, textvariable=self.faltas_var)),
            ("Turno:", tk.OptionMenu(self.frame, self.turno_var, *turnos)),
        ]

        for i, (label, widget) in enumerate(campos):
            tk.Label(self.frame, text=label, bg="light blue").grid(row=i, column=0, sticky="w")
            widget.grid(row=i, column=1, sticky="ew")

    def obtener_datos(self):
        return {
            "dia": self.dia_var.get(),
            "entrada": self.entrada_var.get(),
            "salida": self.salida_var.get(),
            "retardos": self.retardos_var.get(),
            "asistencia": self.asistencia_var.get(),
            "faltas": self.faltas_var.get(),
            "turno": self.turno_var.get()
        }

    def limpiar(self):
        self.dia_var.set("")
        self.entrada_var.set("")
        self.salida_var.set("")
        self.retardos_var.set("")
        self.asistencia_var.set("")
        self.faltas_var.set("")
        self.turno_var.set("")

class AplicacionVacaciones:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Trabajadores y Jornadas")
        self.root.geometry("700x800")
        self.root.configure(bg="light blue")

        self.periodos = [
            "Enero-Febrero", "Marzo-Abril", "Mayo-Junio", "Septiembre-Octubre", "Noviembre-Diciembre"
        ]
        self.periodo_var = tk.StringVar(value=self.periodos[0])
        self.elecciones = {}

        self.trabajador = Trabajador(self.root)
        self.jornada = Jornada(self.root)

        self.crear_widgets()

    def crear_widgets(self):
        periodo_frame = tk.Frame(self.root, bg="light blue")
        periodo_frame.pack(pady=10)

        tk.Label(periodo_frame, text="Periodo vacacional:", bg="light blue").grid(row=0, column=0, sticky="w")
        tk.OptionMenu(periodo_frame, self.periodo_var, *self.periodos).grid(row=0, column=1, sticky="ew")

        tk.Button(self.root, text="Registrar", command=self.registrar_datos).pack(pady=10)

        self.lista_texto = tk.Text(self.root, height=15, width=80, state="disabled")
        self.lista_texto.pack(pady=10)

    def registrar_datos(self):
        datos_trabajador = self.trabajador.obtener_datos()
        datos_jornada = self.jornada.obtener_datos()
        periodo = self.periodo_var.get()
        nombre = datos_trabajador["nombre"]

        if nombre in self.elecciones:
            messagebox.showerror("Error", f"{nombre} ya ha sido registrado.")
            return

        if periodo in [info['periodo'] for info in self.elecciones.values()]:
            messagebox.showerror("Error", f"El periodo '{periodo}' ya está ocupado.")
            return

        if not all(list(datos_trabajador.values()) + list(datos_jornada.values()) + [periodo]):
            messagebox.showerror("Error", "Todos los campos deben ser completados.")
            return

        self.elecciones[nombre] = {
            "trabajador": datos_trabajador,
            "jornada": datos_jornada,
            "periodo": periodo
        }

        messagebox.showinfo("Éxito", f"Datos de {nombre} registrados correctamente.")
        self.actualizar_lista()
        self.trabajador.limpiar()
        self.jornada.limpiar()

    def actualizar_lista(self):
        self.lista_texto.config(state="normal")
        self.lista_texto.delete("1.0", tk.END)
        for nombre, datos in self.elecciones.items():
            self.lista_texto.insert(tk.END, f"{nombre}:\n")
            self.lista_texto.insert(tk.END, f"  Periodo: {datos['periodo']}\n")
            for campo, valor in datos['trabajador'].items():
                self.lista_texto.insert(tk.END, f"  {campo.capitalize()}: {valor}\n")
            for campo, valor in datos['jornada'].items():
                self.lista_texto.insert(tk.END, f"  {campo.capitalize()}: {valor}\n")
            self.lista_texto.insert(tk.END, "-"*60 + "\n")

        self.lista_texto.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionVacaciones(root)
    root.mainloop()
