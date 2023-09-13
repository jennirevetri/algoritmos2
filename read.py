import csv

def read_csv(path): 
    data_list = []
    with open(path,'r') as csvfile: 
        reader = csv.reader(csvfile) 
        header = next(reader) 
        
        for row in reader: 
            dict_data = dict(zip(header,row)) #Uno la cabera con sus respectivos valores en un dict
            data_list.append(dict_data) #Con los Dict asignados, creo una lista de diccionarios

    return data_list 

def id_reservacion(data_list):
    id = 1

    for element in data_list:
        element["Id"] = id
        id+=1

    
