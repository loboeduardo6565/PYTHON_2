

def app():
    cerveza_tipo = 'Patagonia'
    toma_cerveza = True
    
    mostrar_opciones()

    while toma_cerveza:
        
        consulta = input('Usted toma cerveza?')
        consulta = int(consulta)

        if consulta == 1:
            print(f'Lleva las de {cerveza_tipo} por favor')
            toma_cerveza = False
        elif consulta == 2:
            print(f'Lleve lo que vaya a tomar')
            toma_cerveza = False
        else:
            print('Responda la pregunta3 \r\n')

def mostrar_opciones():
    print('Seleccione la opción que desee: \r\n')
    print('1) Si tomo cerveza')
    print('2) No tomo cerveza')

app()