from ex1_classes import Aluno, Turma

pedro = Aluno('Pedro', 16, "Info")
jopepew = Aluno('João Almeida', 67, "Info")
miguel = Aluno("Miguel Garcia Sorrilha Neto", 16, "Info")

info2024 = Turma("INFO24", 2024)
info2024.estudantes.append(pedro)
info2024.estudantes.append(jopepew)
info2024.estudantes.append(miguel)
info2024.exibir_estudante()

# nome = input("Digite o nome do aluno: ")
# idade = int(input("Digite a idade do aluno: "))
# curso = input("Digite o curso do aluno: ")

# aluno1 = Aluno(nome, idade, curso, [7, 10, 8])
# aluno1.apresentar()

# print(f"A média das notas é {aluno1.calcular_media}")
