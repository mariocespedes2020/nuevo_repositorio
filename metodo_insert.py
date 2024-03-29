from tkinter import*

root= Tk() # crear ventana

root.title("aprendizaje con gatos") # titulo vewntana
root.geometry("800x600+368+120") 

# entrada desde teclado con objeto "Entry" hacia la ventana root 
entrada=Entry(root)
entrada.insert(0,"escriba su nombre ")
entrada.bind("<Button-1>",lambda e: entrada.delete(0,E))
entrada.pack()
# evento al pulsar boton funcion
def pulsar_boton():
    nombre = entrada.get() # dato de entrada se almacena en texto con .get()
    Label(root, text=f" nombre =  {nombre}").pack() # rotulo en root  con el texto 
    
    

# boton
''' Button(root, text="pulsar!", command=pulsar_boton()).pack() se quita () despues
de boton de quedar asi Button(root, text="pulsar!", command=pulsar_boton).pack()''' 
Button(root, text="Enviar ", command=pulsar_boton).pack()


# bucle de ejecucion


root.mainloop() # loop continuo en root