#promocao especial
#compras acima de 1.000 recebe 20%
#compras acima de 500 recebem 10%
#compras abaixo de 500 nao recebem desconto

valor_compra = float(input("Digite o valor da compra do cliente: "))

compra_acima_mil = valor_compra * 0.2
compra_acima_quinhentos = valor_compra * 0.1

if valor_compra >= 1000: 
    print (f"Voce conseguiu um desconto de 20%, totalizando: {valor_compra - compra_acima_mil}")
elif valor_compra >= 500:
    print(f"Voce conseguiu um desconto de 10%, totalizando: {valor_compra-compra_acima_quinhentos}")
else:
    print("Sem desconto nenhum!")
    
#entender que o if e uma condicao que se verdadeira, interrompe a sequencia.
#caso a funcao seja falsa, parte para proxima e assim a diante. lembrar que ela sera sera finita

