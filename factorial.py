def factorial(numero):
    resultado=1
    while numero>0:
        resultado=resultado*numero
        numero=numero-1
    return resultado
print (factorial(3))
    