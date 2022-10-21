#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def anhio_bisiesto():
    anhio: int = int(input("Introduce un año: "))
    if(anhio % 4 == 0 and (anhio % 100 != 0 or anhio % 400 == 0)):
        print(f"¡El año {anhio} es bisiesto!")
    else:
        print(f"El año {anhio} NO es bisiesto!")

anhio_bisiesto()