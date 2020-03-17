peso = int(input("Peso: "))
medida = input('(L)bs ou (K)g: ')
if medida.upper() == "L":
   convertido = peso * 0.45
   print(f"Você pesa {convertido} kg")
else:
    convertido = peso / 0.45
    print (f"Você pesa {convertido} lbs")