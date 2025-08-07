from os import system
from time import sleep
while True:
    system("cls")

    print("-"*50)
    print(" "* 15, "SISTEMA - MEU")
    print("-"* 50)
    print("opções funções")
    print(" 1   -  subtração   ")
    print(" 2   -  multiplicar   ")
    print(" 3   -  somar   ")
    print(" 4   -  dividir   ")
    print(" 5   -  SAIR DO SISTEMA   ")
    print("-"*50)

    try:
        opcao=int(input("Escolha uma opção:"))
        if opcao ==1:
            nume1= float(input("Informe o primeiro numero:"))
            nume2= float(input("Informe o segundo numero:"))
            resultado= nume1-nume2
            print(f"A subtração é{resultado}")
        elif opcao ==2:
            nume1= float(input("Informe o primeiro numero:"))
            nume2= float(input("Informe o segundo numero:"))
            resultado= nume1*nume2
            print(f"A multiplicação é{resultado}")
            
        elif opcao ==3:
            nume1= float(input("Informe o primeiro numero:"))
            nume2= float(input("Informe o segundo numero:"))
            resultado= nume1+nume2
            print(f"A soma é{resultado}")
        elif opcao ==4:
            nume1= float(input("Informe o primeiro numero:"))
            nume2= float(input("Informe o segundo numero:"))
            if nume2 !=0:
             resultado= nume1/nume2
             print(f"A divisão é:{resultado}")
            else:
                print("ERRO")
        elif opcao ==5:
            print("opção sair!")
            sleep(1)
            break
        else:
            print("ERRO")
    except ValueError:
        print("valor errado.Digite somente numeros.")
    finally:
        input("Precione para continuar...")
