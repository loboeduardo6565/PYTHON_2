# Otro ejemplo de un falso case con cervezas
def opciones():

    cerveza = str.lower(input('Introduzca la marca de cerveza: \r\n'))

    match cerveza:
        case "patagonia":
            print(f"Usted quiere tomar Cerveza {cerveza}")
        case "quilmes":
            print(f"Usted quiere tomar Cerveza {cerveza}")
        case "corona":
            print(f"Usted quiere tomar Cerveza {cerveza}")
        case _:     # Actua como un else
            print ("No disponemos de esa cerveza")

opciones()


#def http_error(status):
#    match status:
#        case 400:
#            return "Solicitud incorrecta"
#        case 404:
#            return "No encontrado"
#        case 418:
#            return "Soy una tetera"
#        case _:
#            return "Algo anda mal en internet"
#print(http_error(500))