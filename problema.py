
x = int(input("ingrese la medida de X: "))
y = int(input("Ingrese la medida de Y: "))
area_techo = x * y

a = int(input("Ingrese la medida de A: "))
b = int(input("Ingrese la medida de B: "))
area_panel = a * b

max_paneles = area_techo // area_panel

print("La cantidad máxima de paneles es de:", max_paneles)