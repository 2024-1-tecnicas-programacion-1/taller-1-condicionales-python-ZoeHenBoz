def evaluar(peso, estatura, edad):
    imc = peso / (estatura * estatura)
    
    if edad < 45:
        if imc < 22:
            return "bajo"
        elif imc >= 22:
            return "medio"
    else:
        if imc < 22:
            return "medio"
        elif imc >= 22:
            return "alto"

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
