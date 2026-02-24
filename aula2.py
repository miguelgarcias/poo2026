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

# Nas condições utilisamos ELIF e não mais ELSE IF.
# Esse .2f, ele é para ser DUAS casas após o ponto.

# EXERCICIO 1
numero = float(input("Me informe um número: "))

if(numero > 100):
    resultado = numero / 2
    print(f"Seu número é: {resultado}")
else:
    print(f"Seu número é: {numero}")

# EXERCICIO 2
x = int(input("Me informe um número e irei dizer se ele é par ou impar: "))

if(x % 2 == 0):
    print(f"O número {x} é par")
else:
    print("O número {x} é impar.")