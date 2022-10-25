import random

alphaupper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', ' L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphamin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'u', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['@', '#', '$', '%', '&', '#']

randomone = random.choice(alphaupper)
randomtwo = random.choice(alphamin)
randomtree = random.choice(symbol)
randomnumber = random.randint(1,30)
randomnumber = random.randint(1,100)

word = str(input('Digite sua palavra favorita para fazer parte de sua senha:'))


print(f'A senha gerada foi: {word}{randomone}{randomtwo}{randomtree}{randomnumber}')
