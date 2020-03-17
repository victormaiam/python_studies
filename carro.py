comando = ""
carro_ligado = True
while True:
    comando = input("> ").lower()
    if comando == "ligar":
        if carro_ligado:
                print ("Carro já está ligado")
        else:
            carro_ligado = True
            print("Carro ligou...")
    elif comando == "parar":
        if not carro_ligado:
            print("Carro já está parado.")
        else:
            carro_ligado = False
            print ("Carro parado") 
    elif comando == "ajuda":
        print(""")
ligar - para iniciar o carro
parar - para parar o carro
sair - para sair
        """)
    elif comando == "parar":
        break
    else:
        print("Desculpa não entendo o comando...")
        
