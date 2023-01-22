# Definición de función y condicional if numeros pares
def app():
    print('Introduzca un número entero')
    numero = int(input()) # Como preciso un número entero defino la entrada de tipo entero
    if numero > 0:
        print(f'El número: {numero} es mayor que cero, es positivo')
        if numero % 2 == 0:
            print(f'El número: {numero} es par')
        else:
            print(f'El número: {numero} es impar')
    else:
        print(f'El número: {numero} es menor que cero, es negativo')
        if numero % 2 == 0:
            print(f'El número: {numero} es par')
        elif numero % 2 != 0:
            print(f'El número: {numero} es impar')
app()