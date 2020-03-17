''''
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
'''

def calcula_soma(limite):
    soma = 0

    for i in range(0, limite + 1):
        if i%3 == 0 or i%5 == 0:
            soma = soma + i
    return(soma)

limite = 20
soma = calcula_soma(limite)
print(soma)