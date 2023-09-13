
from read import read_csv,id_reservacion
from interfaz import ventana_principal

def run():
    file_path ='reservaciones.csv'
    data_list= read_csv(file_path)
    ventana_principal(data_list)
    id_reservacion(data_list)
    for x in data_list:
        print(x)
    
    
    
run()
