from email.errors import StartBoundaryNotFoundDefect


planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno','Urano', 'Neptuno']
contador = len(planetas)
print("Acontinuacion presentamos la lista de los planetas del sistema solar")
print()
for i in range(contador):
    print("Planeta", i+1, ":",planetas[i])
print()
planetas.append('Pluton')
print(planetas[-1])
print()
contador = len(planetas)
entrada = input("Escribe el nombre de un planeta, la primer letra debera de escribirse con mayuscula: ")
ubicacion = planetas.index(entrada)
print()
print("Los planetas mas sercanos al sol con respecto de", entrada)
print()
rango = contador - ubicacion -1
for i in range(ubicacion):
    print("Planeta", i+1, ":",planetas[i])
print()
print("Los planteas mas lejanos del sol con respecto de", entrada)
print()
for i in range(rango):
    print("Planeta", ubicacion+i+1 , ":",planetas[ubicacion+i+1])
