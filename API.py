import requests
#URL ANTES DEL "?fields"
URL="https://restcountries.com/v3.1/name/"

def get_pais(nombre):
    #url para obtener datos según requiera el usuario
    url = f"{URL}{nombre}?fields=name,population,area,continents"
    #GET para obtener información de la API y cargarla en respuesta
    respuesta = requests.get(url, timeout=5)
    #Comprobando que se ejecute con éxito
    if respuesta.status_code == 200:
        #generando un json de respuesta e ingresando a la lista datos
        datos = respuesta.json()
        print(datos)
        print(datos[0])
        if datos:
            #Guardamos en pais el diccionario de la lista datos
            pais = datos[0]
            #Retornamos la información esencal
            return{
                "nombre": pais["name"]["common"],
                "poblacion": pais["population"],
                "superficie": pais["area"],
                "continente": pais["continents"][0]
            }
        else:
            print("No se encontraron datos para este país.")
    else:
        print("Error al obtener datos:", respuesta.status_code)

#Probando pantalla estética con la información
if __name__ == "__main__":
    def mostrar_datos_pais(info):
        print("\nInformación del país:")
        print(f"País: {info["nombre"]}")
        print(f"Continente: {info["continente"]}")
        print(f"Población: {info["poblacion"]} habitantes")  
        print(f"Superficie: {info["superficie"]} km²")
        print("-" * 50) 
    nombre = input("Ingrese el nombre de un país: ").strip()
    mostrar_datos_pais(get_pais(nombre))





