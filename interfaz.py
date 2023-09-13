from tkinter import *
from tkinter import ttk

datos_globales = {}

def ventana_principal(data_list):
    
    global datos_globales 
    global ventana_principal1

    datos_globales = data_list

    ventana_principal1 = Tk()
    ventana_principal1.resizable(False,False) 
    ventana_principal1.title("Gestion de Hotel")
    ventana_principal1.geometry("800x500")
    ventana_principal1.config(background="LightSteelBlue3")

    titulo = Label(ventana_principal1, text="Gestion de Reservaciones y Ordenamiento", font=("Trispace 20 bold"),bg='LightSteelBlue3',fg="SkyBlue4")
    titulo.pack(pady=12)

    boton1 = Button(ventana_principal1, text="Quicksort: Ordenar por fecha de entrada",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana2)
    boton2 = Button(ventana_principal1, text="Quicksort: Ordenar por nro de habitacion",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana3)
    boton3 = Button(ventana_principal1, text="Quicksort: Ordenar por duracion de estadia",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana4)
    boton4 = Button(ventana_principal1, text="Ordenamiento multiple",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana5)
    boton5 = Button(ventana_principal1, text="Ordenar ascendente",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana6)
    boton6 = Button(ventana_principal1, text="Ordenar descendente",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2)

    boton1.pack(pady=12)
    boton2.pack(pady=12)
    boton3.pack(pady=12)
    boton4.pack(pady=12)
    boton5.pack(pady=12)
    boton6.pack(pady=12)
    ventana_principal1.mainloop()

def ventana2():
    global datos_globales
    ventana2 = Toplevel(ventana_principal1)
    ventana2.geometry("800x500")
    ventana2.title("ventana2")
    ventana2.config(background="LightSteelBlue3")

    botonVolver = Button(ventana2, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana2))
    botonVolver.place(relx=0.65, rely=0.9)
    
    sorting_key_fecha_entrada = lambda x: x.get("fecha_entrada","")
    sorted_data= quicksort(datos_globales,key=sorting_key_fecha_entrada)

    tree = ttk.Treeview(ventana2)
    tree["columns"]= tuple(sorted_data[0].keys())
    
    for column in tree["columns"]:
        tree.heading(column,text=column)
        tree.column(column,width=100)

    for item in sorted_data:
        tree.insert("","end",values=tuple(item.values()))

    tree.pack()

    ventana_principal1.withdraw()
    ventana2.mainloop()


def ventana3():
    global ventana3
    ventana3 = Toplevel(ventana_principal1)
    ventana3.geometry("800x500")
    ventana3.title("ventana3")
    ventana3.config(background="LightSteelBlue3")

    botonVolver = Button(ventana3, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana3))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal1.withdraw()
    ventana3.mainloop()

def ventana4():
    global ventana4
    ventana4 = Toplevel(ventana_principal1)
    ventana4.geometry("800x500")
    ventana4.title("ventana4")
    ventana4.config(background="LightSteelBlue3")

    botonVolver = Button(ventana4, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana4))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal1.withdraw()
    ventana4.mainloop()

def ventana5():
    global ventana5
    ventana5 = Toplevel(ventana_principal1)
    ventana5.geometry("800x500")
    ventana5.title("ventana3")
    ventana5.config(background="LightSteelBlue3")

    botonVolver = Button(ventana5, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana5))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal1.withdraw()
    ventana5.mainloop()

def ventana6():
    global ventana6
    ventana6 = Toplevel(ventana_principal1)
    ventana6.geometry("800x500")
    ventana6.title("ventana3")
    ventana6.config(background="LightSteelBlue3")

    botonVolver = Button(ventana6, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana6))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal1.withdraw()
    ventana6.mainloop()

def ventana7():
    global ventana7
    ventana7 = Toplevel(ventana_principal1)
    ventana7.geometry("800x500")
    ventana7.title("ventana3")
    ventana7.config(background="LightSteelBlue3")

    botonVolver = Button(ventana7, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana7))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal1.withdraw()
    ventana6.mainloop()

def volver_ventana(ventana_secundaria):
    ventana_secundaria.destroy()
    ventana_principal1.deiconify()

def quicksort(data_list, key):
    if len(data_list) <= 1:
        return data_list

    pivot = data_list[len(data_list) // 2]
    less = [x for x in data_list if key(x) < key(pivot)]
    equal = [x for x in data_list if key(x) == key(pivot)]
    greater = [x for x in data_list if key(x) > key(pivot)]

    return quicksort(less, key) + equal + quicksort(greater, key)



    

