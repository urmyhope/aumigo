import os

from cadastropet import Cadastropet

cadpet = Cadastropet()

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

TContinue = True

while TContinue:
    LimpaTela()
    print("+-------------------------------+")
    print("|     1 - Cadastro              |")
    print("|     2 - Fila Preferencial     |")
    print("|     3 - Fila Emergência       |")
    print("|     4 - Sair                  |")
    print("+-------------------------------+")
    Menu = input("      Informe a opção: ")

    if Menu == '1':
        LimpaTela()
        cadpet.cadastro
    elif Menu == '4':
        TContinue = False
