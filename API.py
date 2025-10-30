import requests
import csv
URL="https://restcountries.com/v3.1/all?fields=name,population,area,continents"

def paises_lista():
    #GET para obtener información de la API y cargarla en respuesta
    respuesta = requests.get(URL, timeout=5)
    print (respuesta)
    #Comprobando que se ejecute con éxito
    if respuesta.status_code == 200:
        #generando un json de respuesta e ingresando a la lista datos
        datos = respuesta.json()
        paises_=[]
        for i in range(len(datos)):
            pais= datos[i]
            paises={"nombre":pais["name"]["common"],
            "poblacion":pais["population"],
            "area":pais["area"],
            "continente":pais["continents"][0]}
            paises_.append(paises)
        return paises_#RETORNA LISTA DE FILTRADA POR EL FOR
    else:
        print("Error al obtener datos:", respuesta.status_code)

def paises_csv(lista_paises):
    paises=lista_paises
#INGRESAMOS LA LISTA DE PAÍSES PARA CREAR EL CSV
    with open("C:\\Users\\f\\OneDrive\\Escritorio\\integrador\\prueba2\\paises.csv", "w", newline="", encoding="utf-8") as archivo:
        #ESCRIBIMOS ENCABEZADOS
        escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Población", "Area", "Continente"])
        
        escritor.writeheader()  
#INGRESAMOS LOS PAÍSES SEGÚN LOS ENCABEZADOS AL CSV
        for pais in paises:
            escritor.writerow({
                "Nombre": pais["nombre"],
                "Población": pais["poblacion"],
                "Area": pais["area"],
                "Continente": pais["continente"]
            })
    print("CSV CREADO")

if __name__ == "__main__":

    paises_data=paises_lista()
    paises_csv(paises_data)

