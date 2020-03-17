is_hot = False
is_cold = False

if is_hot:
    print("It`s a hot day.")
    print ("Drink plenty of water.")
elif is_cold:
    print("It`s a cold day.")
    print("Wear warm clothes.")
else:
    print("It`s a lovely day.")
    print("Enjoy your day.")

tem_credito = False
preco = 1000000
preco1 = preco * 0.10  
preco2 = preco * 0.20  

if tem_credito:
    print(preco1)
else:
    print(preco2)
print("Sua entrada é nesse valor.")

if tem_credito:
    entrada = 0.1 * preco
else:
    entrada = 0.2 * preco
print(f"Entrada: R${entrada}" )

tem_salario_alto = True
tem_bom_credito = False

if tem_salario_alto and tem_bom_credito:
    print("Você pode pegar um empréstimo")
else:
    print("Você não pode pegar empréstimo.")

if tem_bom_credito or tem_salario_alto:
    print("Você pode pegar um empréstimo")

temperatura = 30

if temperatura != 30:
    print("É um dia quente!")
else:
    print("Não é um dia quente.")

nome = "Victor"

if len(nome) < 3:
    print("Nome precisa ter 3 caracteres")
elif len(nome) > 50:
    print("Nome só pode ter até 50 caracteres.")
else:
    print("Parece bom!")