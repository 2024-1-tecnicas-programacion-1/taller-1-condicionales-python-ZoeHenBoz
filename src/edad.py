from datetime import date

def evaluar(dia, mes, anno):
    currentDate = date.today()
    diaActual = currentDate.day
    mesActual = currentDate.month
    annoActual = currentDate.year
    edad = 0

    if mes > mesActual or (mes == mesActual and dia > diaActual):
        edad = annoActual - anno - 1
    else:
        edad = annoActual - anno

    return f"Usted tiene {edad} años."

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
