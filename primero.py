print('\r\n Prueba \r\n')

variable_num = 50
print(f'\r\n Variable {variable_num} \r\n')
variable_cadena = "Charlotte"
print(f'\r\n Variable String {variable_cadena} \r\n')

var = True # Booleano True/False

var1, var2, var3 = 3, "valor2", "valor3"
print(f'Valor String 1: {var1}')
print(f'Valor String 2: {var2}')
print(f'Valor String 3: {var3} \r\n')

#Se puede instanciar una constante desde un archivo externo
import constantes
print(constantes.GRAVEDAD)

# Suma ejemplo
print('\r\n suma de dos variables: ', variable_num + var1 )
# Resta ejemplo
print('\r\n resta de dos variables: ', variable_num - var1 )
# Multiplicación ejemplo
print('\r\n multiplicación de dos variables: ', variable_num * var1 )
# división ejemplo
print('\r\n división de dos variables: ', variable_num / var1 )
# producto entero de división ejemplo
print('\r\n producto entero de división de dos variables: ', variable_num // var1 )
# Exponente ejemplo
print('\r\n Exponente: ', variable_num ** var1 )

# Operadores comparativos: 
print('\r\n Variable_num es mayor que var1? : ', variable_num > var1 )
print('\r\n Variable_num es menor que var1? : ', variable_num < var1 )
print('\r\n Variable_num es igual que var1? : ', variable_num == var1 )
print('\r\n Variable_num es desigual que var1? : ', variable_num != var1 )
print('\r\n Variable_num es mayor o igual que var1? : ', variable_num >= var1 )
print('\r\n Variable_num es menor o igual que var1? : ', variable_num <= var1 )



