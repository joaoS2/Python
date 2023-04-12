from random import randint
import os 
import names


#|Desenvolvendo o gerador de cpf|
def cpfGenerator():
    os.system("cls")

    while True:
        #|Gera os 9 primeiros dígitos do cpf aleatoriamente|
        cpf = [randint(0, 9) for x in range(9)]

        #|Verifica se o CPF não é repetido|
        if cpf != cpf[::-1]:
            break
    
    #|Calcula os dígitos verificadores|
    for x in [10, 11]:
        verificator = sum([cpf[x - y] * y for y in range(x, 1, -1)]) * 10 % 11 % 10
        cpf.append(verificator)

    #|Converte os númerod do CPF para string e insere a lista em uma variável|
    cpf="".join([str(x) for x in cpf])

    #|Converte a o cpf para o modo padrão 123-456-789-xy|
    cpfStr = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpfStr

cpf = cpfGenerator()
print(f"CPF: {cpf}")

#|Gerando o número de telefone  
def phoneGenerator():
    os.system("cls")

    while True:
        #|Gera os números de telefone|
        phone1 = [randint(0, 9) for x in range(4)]
        phone2 = [randint(0, 9) for x in range(4)]

        #|Verifica se os números não são iguais|
        if phone1 != phone2[::-1]:
            break


#|Gerar nome e sobrenome|
import names

nome_aleatorio = names.get_full_name()

print(f"Olá, {nome_aleatorio}!")

#|Gerar o e-mail|
