#Pedir o número de telefone e ele retornar escrito por extenso
phone = input("phone:")
numbers = {
    "1": "Um"
    "2": "Dois"
    "3": "Três"    
}
output = ""
for ch in phone:
    output += numbers.get(ch, "!") + " "
print(output)

