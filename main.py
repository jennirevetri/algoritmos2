from tkinter import *
from tkinter import ttk

import csv

def read_csv(path): 
    data_list = []
    with open(path,'r') as csvfile: 
        reader = csv.reader(csvfile) 
        header = next(reader) 
        
        for row in reader: 
            dict_data = dict(zip(header,row)) #Uno la cabera con sus respectivos valores en un dict
            data_list.append(dict_data) #Con los Dict asignados, creo una lista de diccionarios

    return data_list #Retorno la lista de diccionarios
    
if __name__=='__main__':
    file_path ='reservaciones.csv'
    data= read_csv(file_path)
    for row in data:
        print(row)





def ventana_principal():
    global ventana_principal
    ventana_principal = Tk()
    ventana_principal.resizable(False,False) 
    ventana_principal.title("Gestion de Hotel")
    ventana_principal.geometry("800x500")
    ventana_principal.config(background="LightSteelBlue3")

    titulo = Label(ventana_principal, text="Gestion de Reservaciones y Ordenamiento", font=("Trispace 20 bold"),bg='LightSteelBlue3',fg="SkyBlue4")
    titulo.pack(pady=12)

    boton1 = Button(ventana_principal, text="Quicksort: Ordenar por fecha de entrada",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana2)
    boton2 = Button(ventana_principal, text="Quicksort: Ordenar por nro de habitacion",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana3)
    boton3 = Button(ventana_principal, text="Quicksort: Ordenar por duracion de estadia",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana4)
    boton4 = Button(ventana_principal, text="Ordenamiento multiple",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana5)
    boton5 = Button(ventana_principal, text="Ordenar ascendente",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana6)
    boton6 = Button(ventana_principal, text="Ordenar descendente",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2)

    boton1.pack(pady=12)
    boton2.pack(pady=12)
    boton3.pack(pady=12)
    boton4.pack(pady=12)
    boton5.pack(pady=12)
    boton6.pack(pady=12)
    ventana_principal.mainloop()

def ventana2():
    global ventana2
    ventana2 = Toplevel(ventana_principal)
    ventana2.geometry("800x500")
    ventana2.title("ventana2")
    ventana2.config(background="LightSteelBlue3")

    botonVolver = Button(ventana2, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana2))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal.withdraw()
    ventana2.mainloop()


def ventana3():
    global ventana3
    ventana3 = Toplevel(ventana_principal)
    ventana3.geometry("800x500")
    ventana3.title("ventana3")
    ventana3.config(background="LightSteelBlue3")

    botonVolver = Button(ventana3, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana3))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal.withdraw()
    ventana3.mainloop()

def ventana4():
    global ventana4
    ventana4 = Toplevel(ventana_principal)
    ventana4.geometry("800x500")
    ventana4.title("ventana4")
    ventana4.config(background="LightSteelBlue3")

    botonVolver = Button(ventana4, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana4))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal.withdraw()
    ventana4.mainloop()

def ventana5():
    global ventana5
    ventana5 = Toplevel(ventana_principal)
    ventana5.geometry("800x500")
    ventana5.title("ventana3")
    ventana5.config(background="LightSteelBlue3")

    botonVolver = Button(ventana5, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana5))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal.withdraw()
    ventana5.mainloop()

def ventana6():
    global ventana6
    ventana6 = Toplevel(ventana_principal)
    ventana6.geometry("800x500")
    ventana6.title("ventana3")
    ventana6.config(background="LightSteelBlue3")

    botonVolver = Button(ventana6, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana6))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal.withdraw()
    ventana6.mainloop()

def ventana7():
    global ventana7
    ventana7 = Toplevel(ventana_principal)
    ventana7.geometry("800x500")
    ventana7.title("ventana3")
    ventana7.config(background="LightSteelBlue3")

    botonVolver = Button(ventana7, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana7))
    botonVolver.place(relx=0.65, rely=0.9)

    ventana_principal.withdraw()
    ventana6.mainloop()
def volver_ventana(ventana_secundaria):
    ventana_secundaria.destroy()
    ventana_principal.deiconify()

ventana_principal()
    

