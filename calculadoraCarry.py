import tkinter as tk

def agregar_caracter(caracter):
    pantalla.insert(tk.END, caracter)

def calcular():
    try:
        expresion = pantalla.get()
        resultado = eval(expresion)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, resultado)
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora del Carry")

# Establecer tamaño de la ventana
ventana.geometry("190x370")  # Ancho x Alto

# Establecer color de fondo de la ventana
ventana.configure(bg="lightblue")

# Pantalla de entrada
pantalla = tk.Entry(ventana, font=("Arial", 30), justify=tk.RIGHT)
pantalla.pack(fill=tk.BOTH, expand=True)

# Botones para números y operaciones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

botones_numeros = "789456123"
for num in botones_numeros:
    boton = tk.Button(frame_botones, text=num, font=("Arial", 20), command=lambda n=num: agregar_caracter(n))
    boton.grid(row=(9-int(num))//3, column=(int(num)-1)%3, sticky=tk.NSEW)

boton_cero = tk.Button(frame_botones, text="0", font=("Arial", 20), command=lambda: agregar_caracter("0"))
boton_cero.grid(row=3, column=0, sticky=tk.NSEW)

boton_punto = tk.Button(frame_botones, text=".", font=("Arial", 20), command=lambda: agregar_caracter("."))
boton_punto.grid(row=3, column=1, sticky=tk.NSEW)

boton_suma = tk.Button(frame_botones, text="+", font=("Arial", 20), command=lambda: agregar_caracter("+"))
boton_suma.grid(row=0, column=3, sticky=tk.NSEW)

boton_resta = tk.Button(frame_botones, text="-", font=("Arial", 20), command=lambda: agregar_caracter("-"))
boton_resta.grid(row=1, column=3, sticky=tk.NSEW)

boton_multiplicacion = tk.Button(frame_botones, text="*", font=("Arial", 20), command=lambda: agregar_caracter("*"))
boton_multiplicacion.grid(row=2, column=3, sticky=tk.NSEW)

boton_division = tk.Button(frame_botones, text="/", font=("Arial", 20), command=lambda: agregar_caracter("/"))
boton_division.grid(row=3, column=3, sticky=tk.NSEW)

boton_igual = tk.Button(frame_botones, text="=", font=("Arial", 20), command=calcular)
boton_igual.grid(row=4, column=3, sticky=tk.NSEW, rowspan=2)

boton_limpiar = tk.Button(frame_botones, text="C", font=("Arial", 20), command=lambda: pantalla.delete(0, tk.END))
boton_limpiar.grid(row=4, column=0, sticky=tk.NSEW, columnspan=3)

ventana.mainloop()