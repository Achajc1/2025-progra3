def BusquedaBinaria(arr,numero,inicio=0,fin=None):
    
    if fin==None:
        fin=len(arr)-1
    medio=(inicio+fin)//2
    if arr[medio]==numero:
        return medio
   # if arr[medio]>numero:
    #    return BusquedaBinaria(arr,numero,inicio,medio-1)
    #if arr[medio]<numero:
     #   return BusquedaBinaria(arr,numero,medio+1,fin)
    

    #if arr[medio] == numero:
       # return medio
    elif arr[medio] > numero:
        return BusquedaBinaria(arr, numero, inicio, medio - 1)
    else:
        return BusquedaBinaria(arr, numero, medio + 1, fin)

# Lista ordenada y número a buscar
arr = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
x = 8

# Llamada correcta a la función
print(BusquedaBinaria(arr, x))
