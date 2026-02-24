print("Programação Orientada a Objetos")
nome = input("Nome: ") # Input serve como se fosse um Scanner. Porém todo tipo de dado vai ser String.
idade = int(input("Idade: ")) # Aqui colocamos o INT antes do INPUT para o dado for transformado em INT.
salario = float(input("Salario: "))

# print("Olá", nome, ". Você tem", idade, "anos." )
# str formatada
print(f"Olá {nome}. Você tem {idade} anos.") # Você cerca com as chaves e ela vira variável.

if(salario <= 10000):
    print(f"Você ganha mal: R$:{salario:.2f}")
elif(salario <= 20000):
    print(f"Você ganha bem: R$:{salario:.2f}")
else:
    print(f"Você ganha muito bem: R$:{salario:.2f}")