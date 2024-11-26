import random

numero_secreto = random.randint(0,20)

tentativas = 0 


while True:
    
    palpite = int(input ("Digite seu palpite: "))
    
    tentativas += 1
    
    if palpite > numero_secreto:
        print("NUMERO SECRETO E MENOR")
        if tentativas == 3: 
            break
    elif palpite < numero_secreto:
        print("NUMERO SECRETO E MAIOR")
        if tentativas == 3: 
            break
    else:
        print(f"se acertou em {tentativas}")
        
        
        break