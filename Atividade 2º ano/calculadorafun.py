import os
os.system("cls")

#|Definindo as funções|

#|Fazendo a função para somar|
def addition (a,b):
    return a + b

#|Fazendo a função de subtração|
def subtraction (a,b):
    return a - b

#|Fazendo a função de multiplicação|
def multiplication(a,b):
    return a * b

#|Fazendo a função de multiplicação|
def division(a,b):
    return a / b
    
#|Fazendo o Menu|
def menu():
    print("Now choose the operation to be performed")
    print("A-Addition")
    print("S-Subtraction")
    print("M-Multiplication")
    print("D-Division")
    print("E-Exit")
    
#|Criando a função para a calculadora|
def calculator():
    os.system("cls")

    menu()

    option = input("Enter the desired operation: ").upper()
    os.system("cls")

    #|Teste lógico|
    if option == "A" or option == "ADDITION":
            result = addition(num1,num2)
            print("_" * 20)
            print("|" f"{num1} + {num2} = {result:.1f}" "|")
            print("_" * 20) 
            
    elif option == "S" or (option == "SUBTRACTION"):
            result = subtraction(num1,num2)
            print("_" * 20)
            print("|" f"{num1} - {num2} = {result:.1f}" "|")
            print("_" * 20) 
    elif option == "M" or option == "MULTIPLICATION":
            result = multiplication(num1,num2)
            print("_" * 20)
            print("|" f"{num1} x {num2} = {result:.1f}" "|")
            print("_" * 20) 

    elif option == "D" or option == "DIVISION":
            result = division(num1,num2)
            print("_" * 20)
            print("|" f"{num1} ÷ {num2} = {result:.1f}" "|")
            print("_" * 20) 

    elif option == "E" or option == "EXIT":
            print("Closing the calculator... \n See you latter <3")

        #|Caso a letra inserida não corresponder com a operações|
    else:
        changeLetter()
def changeLetter():
    os.system("cls")
    print("The letter entered does not match any of the operations listed above :c")
    print()
    repeatLatter = input("do you want to change leatter? \n Y-Yes \n N-No \n Your answer: ").upper()
    #|Caso ele queira mudar a letra inserida|
    if repeatLatter == "Y" or repeatLatter == "YES":
        while repeatLatter == "Y" or repeatLatter == "YES":
            repeatLatter = input("Confirm that you really want to change the option by entering ""C-Confirm"": ").upper()
            calculator()

    #|Caso ele não queira mudar as letras inseridas|
    elif repeatLatter == "N" or repeatLatter == "NO":
        os.system("cls")
        repeatLatter = input("Are you sure you don't want to change the letters? \n Y-YES \n N-NO \n You answer: ").upper()

        #|Caso ele não queira alterar a letra inserida|
        if repeatLatter == "Y" or repeatLatter == "YES":
                os.system("cls")
                print("Closing the calculator... \n See you latter <3")

        #|Caso ele queira alterar a letra inserida|
        elif repeatLatter == "N" or repeatLatter == "NO":
            while repeatLatter == "N" or repeatLatter == "NO":
                repeatLatter = input("Confirm that you really want to change the option by entering ""C-Confirm"": ").upper()
                calculator()
#|Definindo as variáveis|
num1 : float
num2: float
option : float
result : float
repeat : str
repeatLatter : str


#|Entradada de Dados|
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

os.system("cls")

#|Caso o número seja zero|
if num1 == 0 or num2 == 0:
    print("0 cannot be divided by any number! <:O")
    print()
    repeat = input("do you want to change numbers?? \n Y-Yes \n N-No \n Your answer: ").upper()

    #|Repita todo o código caso o número inserido seja igual a "0" e ele queira mudar|
    if repeat == "Y" or repeat == "YES":
        while repeat == "Y" or repeat == "YES":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num1 == 0 and num2 == 0:
                os.system("cls")
            if num1 != 0 and num2 != 0:
                repeat = input("confirm the numbers by entering the letter ""C"": ").upper()
                calculator()

    #|Caso na veriável "repeat" seja escolhido NÃO|
    elif repeat == "N" or repeat == "NO":
        os.system("cls")
        repeat = input("Are you sure you don't want to change the numbers? \n Y-YES \n N-NO \n You answer: ").upper()
        
        #|Caso ele não queira alterar o número inserido|
        if repeat == "Y" or repeat == "YES":
            print("Closing the calculator... \n See you latter <3")
        
        #|Caso ele queira alterar o número inserido|
        elif repeat == "N" or repeat == "NO":
                while repeat == "N" or repeat == "NO":
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    if num1 == 0 and num2 == 0:
                        os.system("cls")
                    if num1 != 0 and num2 != 0:
                        repeat = input("confirm the numbers by entering the letter ""C"": ").upper()
                        calculator()
                        
#|Caso o número seja diferente de zero|
else:
    calculator()