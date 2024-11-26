senha = '123456789'

login = input("Qual sua senha?")

while senha != login:
    print("voce errou sua senha, tente novamente")
    login = input("Qual sua senha?")
else: 
    print("voce acertou")