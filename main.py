
from read import read_csv
from interfaz import ventana_principal

def run():
    file_path ='reservaciones.csv'
    data_list= read_csv(file_path)
    

    for row in data_list:
        print(row)

    ventana_principal(data_list)
    
    
    
run()
