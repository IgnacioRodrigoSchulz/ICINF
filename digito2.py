#hola mundoooooo
num=int(input("Ingrese un número:"))
if num > 1 and num < 10:
    print("El número tiene un digito...")
else:
   if num >= 10 and num < 100: 
    print("El número tiene dos digitos...")
   else:
      if num >= 100 and num < 1000:
        print("El número tiene tres digitos...")
      else:
         if num >= 1000 and num < 10000:
            print("El número tiene cuatro digitos...")