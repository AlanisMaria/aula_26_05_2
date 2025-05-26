class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso


a1 = Aluno("Miguel", "244", "TDS")
a2 = Aluno("Eliza","345", "ADM")

print(a1.nome, a1.matricula, a1.curso)
print(a2.nome, a2.matricula, a2.curso)
