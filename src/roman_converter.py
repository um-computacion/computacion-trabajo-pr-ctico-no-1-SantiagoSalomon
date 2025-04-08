def decimal_a_romano(num):
    
    if not 1 <= num <= 3999:
        return "El número tiene que estar entre 1 y 3999. Intente denuevo."
    
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letras = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    resultado = ''
    i = 0
    
    while num > 0:
        
        repeticiones = num // numeros[i]
        resultado += letras[i] * repeticiones
        num %= numeros[i]
        
        i += 1
    return resultado

while True:
        entrada = input("Ingresar un número entre 1 y 3999: ")
        num_usuario = int(entrada)
        if 1 <= num_usuario <= 3999:
            resultado = decimal_a_romano(num_usuario)
            print(f"El número {num_usuario} en números romanos es: {resultado}")
            break
        else:
            print("El número tiene que estar entre 1 y 3999. Intente denuevo.")






