def showNumbers(limit):
    for i in range(0, limit+1):
        if i%2 == 0:
            print(f"{i} Par")
        else:
            print(f"{i} Impar")

limit = 10
(showNumbers(limit))