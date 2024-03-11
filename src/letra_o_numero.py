def evaluar(caracter):
    if caracter.isalpha():
        if caracter.isupper():
            return "Es letra mayúscula."
        else:
            return "Es letra minúscula."
    elif caracter.isdigit():
        return "Es número."
    else:
        return "No es letra ni número."

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
