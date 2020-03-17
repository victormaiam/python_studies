secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Jogador: '))
    guess_count += 1
    if guess == secret_number:
        print('Você ganhou!')
        break
else:
    print('Você errou, tente de novo!')