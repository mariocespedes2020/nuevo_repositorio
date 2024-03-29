import tkinter as tk  # importar lib tkinter y nombrarla como tk


root= tk.Tk()  # crear ventana general 
#creacion de etiqueta con "label" llamada mensaje
mensaje=tk.Label(root,text="Mundo gato")
# mostrar etiqueta mensaje con texto "Mundo gato"
mensaje.pack()

root.mainloop() # mantener el loop de ventana (root)
