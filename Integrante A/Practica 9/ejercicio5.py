areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitación2", 12, "rebedor", 4.23]
#imprime el segundo elemento
print(areas[1])
#imprime el ultimo elemento del array
print(areas[len(areas)-1])
#imprime el area de la terrassa
print(areas[5])
#imprime los 3 primeros elementos del array
print(areas[:3])
#imprime del tercer elemento al ultimo
print(areas[2:14])
#imprime el total del area de las 2 habitaciones
print(areas[9]+areas[11])
#modifica el area del lavabo e imprime la nueva lista area
areas[7] = 9
print(areas)
#agrega el area de patio interior y 2.28 en la ultima pisicion y lo imprime
areas.extend(["pati_interior", 2.78])
print(areas)
