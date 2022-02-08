tierra =  149597870
jupiter = 778547200
distancia = jupiter - tierra
print(distancia)
print(int(distancia//1.609344))
print("------------------------")
print()
print("Este es un programa que calcula la distancia entre 2 planetas segun la distancia del Sol")
print()
entrada = input("Escribe la distancia en Km del 1er planeta: ")
primer = int(entrada)
entrada = input("Escribe la distancia en Km del 2do planeta: ")
segundo = int(entrada)
distanciaKm = abs(primer - segundo)
distanciaMilla = distanciaKm * 0.621
print("La distancia del 1er planeta con respecto del 2do es:", distanciaKm, "Km o", distanciaMilla, "Millas")