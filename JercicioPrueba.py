#Calculara el area de un trapezoide
#Michel A. Dionne Gutierrez
a=float(input("Dame la medida de la base mayor"))
b=float(input("Dame la medida de la altura"))
c=float(input("Dame la medida de la base del triangulo izquierdo"))
d=float(input("Dame la medida de la base del triangulo derecho"))
at=((a+(a-(c+d)))/2)*b
print("El area total es de",at,"metros cuadrados")
print("El costo es de ",at*3450,"pesos")