from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

datos_globales = {}
orden_ascendente = False

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
    boton4 = Button(ventana_principal1, text="Mergersort: Ordenamiento descendente y ascendente",font="Trispace 14 bold ",fg="snow",bg="SkyBlue4",width=35,height=2,command=ventana5)
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
    ventana2.title("Quicksort: Fecha Entrada")
    ventana2.config(background="LightSteelBlue3")

    botonVolver = Button(ventana2, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana2))
    botonVolver.place(relx=0.65, rely=0.9)
    
    def extraer_fecha_entrada(item):
        return item.get("fecha_entrada","")
    
    sorted_data= quicksort(datos_globales,key=extraer_fecha_entrada)

    tree_frame = Frame(ventana2)
    tree_frame.pack(pady=60)

    tree_scroll= Scrollbar(tree_frame)
    tree_scroll.pack(side="bottom",fill="x")

    tree = ttk.Treeview(tree_frame,xscrollcommand=tree_scroll.set)
    tree.pack()

    tree_scroll.config(command=tree.xview,orient="horizontal")
    
    
    tree["columns"]= tuple(sorted_data[0].keys())
    
    
    for column in tree["columns"]:
        tree.heading(column,text=column)
        tree.column(column,width=100)

    for item in sorted_data:
        tree.insert("","end",values=tuple(item.values()))

    

    ventana_principal1.withdraw()
    ventana2.mainloop()


def ventana3():
    global datos_globales
    ventana3 = Toplevel(ventana_principal1)
    ventana3.geometry("800x500")
    ventana3.title("ventana3")
    ventana3.config(background="LightSteelBlue3")

    botonVolver = Button(ventana3, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana3))
    botonVolver.place(relx=0.65, rely=0.9)

    def extraer_numero_habitacion(item):
        return item.get("nro_habitacion","")
    
    sorted_data= quicksort(datos_globales,key=extraer_numero_habitacion)

    tree_frame = Frame(ventana3)
    tree_frame.pack(pady=60)

    tree_scroll= Scrollbar(tree_frame)
    tree_scroll.pack(side="bottom",fill="x")

    tree = ttk.Treeview(tree_frame,xscrollcommand=tree_scroll.set)
    tree.pack()

    tree_scroll.config(command=tree.xview,orient="horizontal")
    
    
    tree["columns"]= tuple(sorted_data[0].keys())
    
    
    for column in tree["columns"]:
        tree.heading(column,text=column)
        tree.column(column,width=100)

    for item in sorted_data:
        tree.insert("","end",values=tuple(item.values()))

    

    
    ventana_principal1.withdraw()
    ventana3.mainloop()

def ventana4():
    global datos_globales
    ventana4 = Toplevel(ventana_principal1)
    ventana4.geometry("800x500")
    ventana4.title("ventana4")
    ventana4.config(background="LightSteelBlue3")

    botonVolver = Button(ventana4, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana4))
    botonVolver.place(relx=0.65, rely=0.9)

    def extraer_duracion_estadia(item):
        return item.get("duracion_estadia","")
    
    sorted_data= quicksort(datos_globales,key=extraer_duracion_estadia)

    tree_frame = Frame(ventana4)
    tree_frame.pack(pady=60)

    tree_scroll= Scrollbar(tree_frame)
    tree_scroll.pack(side="bottom",fill="x")

    tree = ttk.Treeview(tree_frame,xscrollcommand=tree_scroll.set)
    tree.pack()

    tree_scroll.config(command=tree.xview,orient="horizontal")
    
    
    tree["columns"]= tuple(sorted_data[0].keys())
    
    
    for column in tree["columns"]:
        tree.heading(column,text=column)
        tree.column(column,width=100)

    for item in sorted_data:
        tree.insert("","end",values=tuple(item.values()))
    ventana_principal1.withdraw()
    ventana4.mainloop()

def validar_fechas(fecha_inicial, fecha_final):
        try:
            fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d")
            fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d")
            return fecha_inicial, fecha_final
        except ValueError:
            return None, None

def ventana5():
    global datos_globales
    global orden_ascendente
    orden_ascendente = True  # Establecer el orden inicial como ascendente

    ventana5 = Toplevel(ventana_principal1)
    ventana5.geometry("800x500")
    ventana5.title("Ordenar por rango de fechas")
    ventana5.config(background="LightSteelBlue3")

    botonVolver = Button(ventana5, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana5))
    botonVolver.place(relx=0.65, rely=0.9)

    fecha_inicial_label = Label(ventana5, text="Fecha Inicial:")
    fecha_inicial_label.pack()
    fecha_inicial_entry = Entry(ventana5)
    fecha_inicial_entry.pack()

    fecha_final_label = Label(ventana5, text="Fecha Final:")
    fecha_final_label.pack()
    fecha_final_entry = Entry(ventana5)
    fecha_final_entry.pack()

    ordenar_ascendente_button = Button(ventana5, text="Ascendente", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: ordenar_tabla(True))
    ordenar_ascendente_button.pack()

    ordenar_descendente_button = Button(ventana5, text="Descendente", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: ordenar_tabla_2(False))
    ordenar_descendente_button.pack()
    limpiar = Button(ventana5, text="Limpiar", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command = lambda : limpiar())
    limpiar.pack()

    

    def ordenar_tabla(ascendente):
        ordenar_descendente_button.config(state=DISABLED)
        ordenar_ascendente_button.config(state=DISABLED)
        
        
        global orden_ascendente
        fecha_inicial = fecha_inicial_entry.get()
        fecha_final = fecha_final_entry.get()

        if fecha_inicial and fecha_final:
            fecha_inicial, fecha_final = validar_fechas(fecha_inicial, fecha_final)
            if fecha_inicial is None or fecha_final is None:
                messagebox.showerror("Error", "Fechas ingresadas no válidas")
                return

        # Filtrar y ordenar las reservaciones según el orden especificado
        def filtro_rango_fechas(item):
            
            fecha_entrada = datetime.strptime(item.get("fecha_entrada", ""), "%Y-%m-%d")
            return fecha_inicial <= fecha_entrada <= fecha_final

        reservaciones_filtradas = list(filter(filtro_rango_fechas, datos_globales))

        # Utilizar mergesort para ordenar las reservaciones
        sorted_data = mergesort(reservaciones_filtradas, ascendente)

        # Si el orden actual es descendente, cambiar a ascendente y viceversa
        # if ascendente!= orden_ascendente:
        #     orden_ascendente = ascendente

        # Actualizar el Treeview con los datos ordenados
        actualizar_treeview(ventana5, sorted_data)

    # ordenar_tabla(True)



    def ordenar_tabla_2(ascendente):
        ordenar_ascendente_button.config(state=DISABLED)
        
        ordenar_descendente_button.config(state=DISABLED)
        
        global orden_ascendente
        fecha_inicial = fecha_inicial_entry.get()
        fecha_final = fecha_final_entry.get()

        if fecha_inicial and fecha_final:
            fecha_inicial, fecha_final = validar_fechas(fecha_inicial, fecha_final)
            if fecha_inicial is None or fecha_final is None:
                messagebox.showerror("Error", "Fechas ingresadas no válidas")
                return

        # Filtrar y ordenar las reservaciones según el orden especificado
        def filtro_rango_fechas(item):
            
            fecha_entrada = datetime.strptime(item.get("fecha_entrada", ""), "%Y-%m-%d")
            return fecha_inicial <= fecha_entrada <= fecha_final

        reservaciones_filtradas = list(filter(filtro_rango_fechas, datos_globales))

        # Utilizar mergesort para ordenar las reservaciones
        sorted_data = mergesort(reservaciones_filtradas, ascendente)

        # Si el orden actual es descendente, cambiar a ascendente y viceversa
        # if ascendente!= orden_ascendente:
        #     orden_ascendente = ascendente

        # Actualizar el Treeview con los datos ordenados
        actualizar_treeview(ventana5, sorted_data)

    # ordenar_tabla(True)
    def limpiar():
        ordenar_ascendente_button.config(state=NORMAL)
        ordenar_descendente_button.config(state=NORMAL)
        tree_frame.destroy()
        
        

    

     

    


    

def mergesort(data_list, ascendente):
    if len(data_list) <= 1:
        return data_list

    # Dividir la lista en dos mitades
    middle = len(data_list) // 2
    left_half = data_list[:middle]
    right_half = data_list[middle:]

    # Llamar recursivamente a mergesort en ambas mitades
    left_half = mergesort(left_half, ascendente)
    right_half = mergesort(right_half, ascendente)

    # Combinar ambas mitades ordenadas
    sorted_data = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if (left_half[left_index]["fecha_entrada"] < right_half[right_index]["fecha_entrada"]) if ascendente else (left_half[left_index]["fecha_entrada"] > right_half[right_index]["fecha_entrada"]):
            sorted_data.append(left_half[left_index])
            left_index += 1
        else:
            sorted_data.append(right_half[right_index])
            right_index += 1

    sorted_data.extend(left_half[left_index:])
    sorted_data.extend(right_half[right_index:])

    return sorted_data

def actualizar_treeview(ventana, data):
    global tree_frame
    tree_frame = Frame(ventana)
    tree_frame.pack(pady=60)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side="bottom", fill="x")

    tree = ttk.Treeview(tree_frame, xscrollcommand=tree_scroll.set)
    tree.pack()

    tree_scroll.config(command=tree.xview, orient="horizontal")

    tree["columns"] = tuple(data[0].keys())

    for column in tree["columns"]:
        tree.heading(column, text=column)
        tree.column(column, width=100)

    

    for item in data:
        tree.insert("", "end", values=tuple(item.values()))

def ventana6():
    global ventana6
    ventana6 = Toplevel(ventana_principal1)
    ventana6.geometry("800x500")
    ventana6.title("ventana3")
    ventana6.config(background="LightSteelBlue3")

    botonVolver = Button(ventana6, text="VOLVER", font="Trispace 14 bold ", fg="snow", bg="SkyBlue4", width=20, command=lambda: volver_ventana(ventana6))
    botonVolver.place(relx=0.65, rely=0.9)

    botonAscendente = Button(ventana6, text="Ascendente", font="Trispace 14 bold", fg="snow", bg="SkyBlue4", width=20, command=lambda: ordenar_tabla(True))
    botonAscendente.pack()

    botonDescendente = Button(ventana6, text="Descendente", font="Trispace 14 bold", fg="snow", bg="SkyBlue4", width=20, command=lambda: ordenar_tabla(False))
    botonDescendente.pack()

    

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



    

