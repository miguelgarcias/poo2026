#def verifica_par(x):
#    if(x % 2 == 0):
#        return True
#    return False
#
#x = int(input("Digite um númer: "))
#
#if(verifica_par(x)):
#    print(f"O {x} é par")
#else:
#    print(f"O {x} não é par")

opc = 0
while(opc != 4):
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Aplicar Desconto")
    print("4 - Sair do programa")
    opc = int(input("Digite um número de 1 á 4: "))
    if(opc == 1):
        print("1 - Cadastrar Produto")
    elif(opc == 2):
        print("2 - Listar Produtos")
    elif(opc == 3):
        print("3 - Aplicar Desconto")
    elif(opc == 4):
        print("4 - Sair do programa")
    else:
        print("Opção Invalida.")