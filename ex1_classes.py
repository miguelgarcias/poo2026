class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.ra = ""
        # self.notas = notas

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e faço o curso de {self.curso}.")
        # while(self.ra == ""):
        #    input("Informe o RA: ")

        print(f"O RA do aluno é: {self.ra}")
    
    def calcular_media(self):
        soma = 0.0
        for i in range(0, len(self.notas)):
            soma += self.notas(i)
        media = soma/len(self.notas)
        return media
    
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
         self.disponivel = False
         print("Livro emprestado com sucesso")
        else:
            print("Livro já está emprestado")

    def devolver(self):
        self.disponivel = True
        print("Livro devolvido com sucesso")

livro = Livro("Dom Casmurro")

livro.emprestar()
livro.emprestar()
livro.devolver()

class Turma:
    
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.estudantes = []
    
    def apresentar(self):
        print(f"{self.nome}")

    def exibir_estudante(self):
        for aluno in self.estudantes:
            aluno.apresentar()