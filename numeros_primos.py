
num_final = 1500 ##Asignacion de un valor entero a la variable num_final##

def si_primo (num_final): ##Función para verificar si es numero primo##
    if num_final < 2: ##Si numero_final(1500) es menor 2## 
        return False ##Devuelve False##
    for i in range(2, num_final): ##Bucle For desde 2 hasta num_final##
        if num_final % i == 0: ##Si el residuo de num_final entre i es igual a cero##
            return False ##Devuelve False##
    return True ##Sino aplica ni al condicional if y al bucle for, entonces retorna True##

### Impresión de los números primos dado un numero n ###

for numeros in range(2,num_final): ##Bucle for desde el 2 hasta num_final##
    if si_primo(numeros): ##ejecuta la función si_primo##
        print(numeros) ##imprime los números primos de acuerdo a la función aplicada##
