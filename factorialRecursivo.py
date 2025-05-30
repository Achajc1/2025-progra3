def factorialRecursivo(numero):
    if numero==0:
        return 1
    else:
        return numero*factorialRecursivo(numero-1)
print(factorialRecursivo(5))