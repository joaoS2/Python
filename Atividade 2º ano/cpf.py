from random import randint
import os 

#Créditos:
#https://youtu.be/bXX_rQOldeM-Luis Fernando Santos Cardeal


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


repeat = input("\nDo you approve the generated CPF? \n Y-YES,I APPROVE \n N-I DON'T APPROVE \n YOU ANSOWER: ").upper()

if repeat in ("Y", "YES"):
    os.system("cls")
    print(f" excellent!\n Your CPF: {cpf}")

elif repeat in ("N" , "NO"):
    os.system("cls")
    repeatCPF = input("Do you want to generate another cpf? \n Y-YES \n N-NO \n YOU ANSOWER: ").upper()

    if repeatCPF in ("Y" ,"YES"):
        while repeatCPF in ("Y" ,"YES"):
            cpf = cpfGenerator()
            os.system("cls")
            print(f"Your New CPF: {cpf}")
            repeat = input("\nDo you approve the generated CPF? \n Y-I APPROVE \n N-I DON'T APPROVE \n YOU ANSOWER: ").upper()
            if repeat in ("Y" , "YES"):
                os.system("cls")
                print(f" excellent!\n Your CPF: {cpf}")
                repeatCPF = input("\n Do you want to confirm this CPF?? \n C-Confirm \n N-NO \n YOU ANSOWER: ").upper()
            elif repeat in ("N" ,"NO"):
                os.system("cls")
                repeatCPF = input("Do you want to confirm this CPF?? \n C-Confirm \n N-NO \n YOU ANSOWER: ").upper()

    #|Caso ele não queira alterar o CPF gerado anteriormente|
    if repeatCPF == "C":
        os.system("cls")
        print(f" excellent!\n Your CPF: {cpf}")

    elif repeatCPF in ("N" ,"NO"):
        os.system("cls")
        print(f"CPF: {cpf}")
        #|ATENÇÂO! MENSAGEM NADA PESSOAL!|
        print("Sorry for not being enough for you :c")


    else:
        os.system("cls")
        print("The selected option does not exist!")

else:
    os.system("cls")
    print("The selected option does not exist!")
