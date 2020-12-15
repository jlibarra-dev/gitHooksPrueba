print("Aprendiendo manejo de excepciones")


def division(numerador, denominador):
    try:
        print(numerador/denominador)
    except ZeroDivisionError:
        print("No se puede dividir por 0. Cambiar el denominador")
    else:
        print("Su division fue exitosa.")
    finally:
        print("Operacion finalizada.")


division(5, 0)

x = -1

if(x < 0):
    raise Exception("No se reciben numeros menores a 0")

print("Prueba Git Hook")
