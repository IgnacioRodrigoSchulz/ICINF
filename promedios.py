nota1 = float(input("Ingresa la primera nota:"))
nota2 = float(input("Ingresa la segunda nota:"))
nota3 = float(input("Ingresa la tercera nota:"))
nota4 = float(input("Ingresa la cuarta nota:"))
suma = nota1+nota2+nota3+nota4
prom = suma/4
if prom == 7:
    print("Aprobado")
else:
    print("Reprobado")