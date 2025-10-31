#Script de Menú con llamado a funciones e importación de módulos
from API import paises_lista
from Buscar_por_nombre import buscar_pais
from funciones_filtrado import filtrar_continente,filtrar_valor
from funciones_ordenamiento import ordenar_paises
from estadisticas import mayor_menor_poblacion, funcion_promedio

def menu():
    paises = paises_lista()
    print(paises)
    bandera=True
    while bandera==True:
        print("\n=== MENÚ DE OPCIONES ===")
        print("1. Buscar país por nombre")
        print("2. Filtrar países")
        print("3. Ordenar países")
        print("4. Mostrar estadísticas")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del país: ")
                buscar_pais(paises, nombre)
            case "2":
                print("\nOpciones de filtrado:")
                print("a. Por continente")
                print("b. Por rango de población")
                print("c. Por rango de superficie")
                opc = input("Seleccione una opción: ")
                match opc:
                    case "a":
                        continente = input("Ingrese el continente: ")
                        filtrar_continente(paises, continente)
                    case "b":
                        min_poblacion = int(input("Población mínima: "))
                        max_poblacion = int(input("Población máxima: "))
                        filtrar_valor(paises,"poblacion", min_poblacion, max_poblacion)
                    case "c":
                        min_area = int(input("Superficie mínima: "))
                        max_area = int(input("Superficie máxima: "))
                        filtrar_valor(paises,"area", min_area, max_area)

            case "3":
                paises_ordenados=[]
                print("\nOpciones de ordenamiento:")
                print("a. Por nombre")
                print("b. Por población")
                print("c. Por superficie")
                categoria = input("Seleccione opción: ").lower()
                match categoria:
                    case "a":criterio="nombre"
                    case "b":criterio="poblacion"
                    case "c":criterio="area"
                    case _:bandera=False
                    
                orden = input("Ascendente (a) o descendente (d)? ").lower() 
                match orden:
                    case "a":orden=False
                    case "d":orden=True
                    case _:bandera=False
                paises_ordenados=ordenar_paises(paises, criterio, orden)
                print(paises_ordenados)

            case "4":
                print("\nOpciones de estadísticas:")
                print("a. País con mayor y menor población")
                print("b. Promedio de población")
                print("c. Promedio de superficie")
                print("d. Cantidad de países por continente")
                seleccion:str = input("Seleccione opción: ").lower()
                match seleccion:
                    case "a": mayor_menor_poblacion(paises)
                    case "b": funcion_promedio(paises,"poblacion")
                    case "c": funcion_promedio(paises,"area")
            case "5":
                print("¡Hasta luego!")
                bandera=False
            case _:
                print(" Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()