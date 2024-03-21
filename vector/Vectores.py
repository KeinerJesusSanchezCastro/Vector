#1.Declarar una lista vacía
lista_vacia = []

#2. Declarar una lista con más de 5 elementos
lista_elementos = [1, 2, 3, 4, 5, 6,7]

#3. Encuentre la longitud de su lista
print("la longitud de la lista con más de cinco elementos:", len(lista_elementos))

#4.Obtener el primer elemento, el elemento central y el último elemento de la lista

primer_elemento = lista_elementos[0]
print(primer_elemento)
elemento_central = lista_elementos[len(lista_elementos)//2]
print(elemento_central)
ultimo_elemento = lista_elementos[-1]
print(ultimo_elemento)


#5. Declara una lista llamada tipos_datos_mezclados, pon tu(nombre, edad, altura, estado civil, dirección)
tipos_datos_mezclados = ["keiner", 23, 1.65, "soltero", "zaragocilla"]

#6. Declare una variable de lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon
it_companies = []
it_companies.insert(0,"Facebook")
it_companies.insert(1,"google")
it_companies.insert(2,"microsoft")
it_companies.insert(3,"apple")
it_companies.insert(4,"IBM")
it_companies.insert(5,"oracle")
it_companies.insert(6,"Amazon")
print(it_companies )

#7.Añadir una empresa de TI a it_companies utilizando los metodos de insercion.
it_companies.append("Movistar")
print("la empresas de TI después de añadir movistar con append:", it_companies)

#8.Comprobar si una determinada empresa existe en la lista it_companies.
verificar = "Microsoft" in it_companies 

#9.Ordena la lista con el método sort()
it_companies.sort()
print(it_companies)

#10. Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()
print( it_companies)

#11.Elimine la primera empresa informática de la lista.
del it_companies[0]
print(it_companies)

#12. Eliminar todas las empresas de TI de la lista 
it_companies.clear()
print(it_companies)
