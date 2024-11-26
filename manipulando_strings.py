frase = "O nome de jesus e recentemente citado na biblia"

if "jesus" in frase:
    print("Sim, essa palavra tem na frase")
    
    
frase1 = "               eu te amo"

print(frase1.strip())

frase2 = "Ola como vai voce"

print(frase2.split())

frase3 = ['Ola', 'como', 'vai', 'voce']

palavras = " ".join(frase3)

print(palavras)

nome = "Alice"
idade = 25
altura = 1.65
mensagem = f"Olá, meu nome é {nome}. Tenho {idade} anos e minha altura é {altura:.2f}"
print (mensagem)
 
texto01 = "Ola mundo"

texto_upper = texto01.upper()
print (texto_upper)

texto_lowwer = texto01.lower()
print (texto_lowwer)