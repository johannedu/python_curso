linha = 0

# Continua o loop externo enquanto 'linha' for menor que 3
while linha < 3:
    
    # Inicializa a variável 'coluna' com o valor 0 para cada nova iteração do loop externo
    coluna = 0

    # Continua o loop interno enquanto 'coluna' for menor que 3
    while coluna < 3:
        
        # Imprime os valores atuais de 'linha' e 'coluna'
        print("Linha: ", linha, " - Coluna: ", coluna)
        
        # Incrementa 'coluna' em 1 para a próxima iteração do loop interno
        coluna += 1

    # Incrementa 'linha' em 1 para a próxima iteração do loop externo
    linha += 1
