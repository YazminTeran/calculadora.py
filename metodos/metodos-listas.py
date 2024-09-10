lista = list (["hola","soy", "Yazmin", 1999 ,12 , 8, True])  
# nos devulve la longitud de la lista cantidad de caracteres
cadena = "hola"
resultado = len(lista)
# Agregado un lemento a la lita 
lista.append("Dioseny")
#agregando un elemento en una posicion especifica
lista.insert(3,"teran")
# agregando varios elementos a la lista
lista.extend(["canal de youtube"])
#eliminando elementos de la lista
lista.pop(-1)
print(len(lista))
lista.pop(0)
#Eliminando un elemento de la lista por su valor
print(len(lista))
lista.remove(1999)
print (lista) 

#([ ])
# ordena los elementos de la lista mietras la lita tenga numeros enteros y boleanos
lista2= list([ 1999, 5, 2, False])
lista2.append(696966)
lista2.sort()
print(lista2)
lista2.sort(reverse=True)
# verificado si un elemento se encuentra en la lisa
elemento_encontrado= lista2.index(2)
print(elemento_encontrado)
print(lista2)

                                                                                                                                                    