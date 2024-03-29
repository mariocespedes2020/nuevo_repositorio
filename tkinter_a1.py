from tkinter import * # importar lib tkinter todo (*)


root= Tk()  # crear ventana general 
root.title(" Gatas aprendiendo") #titulo de ventana (root)
# cambiar tamaño de ventana (root)
root.geometry("800x600+368+120") # (800x600) tamaño venta en px (+500+120) posicion en x , y  en px



#creacion de etiqueta con "label" llamada mensaje
mensaje=Label(root,text="Mundo gato")
mensaje1=Label(root,text="Mundo perro")
# utlizacion de "grid" "row" "column"
mensaje.grid(row=0, column=0)
mensaje1.grid(row=1,column=0)

root.mainloop() # mantener el loop de ventana (root)