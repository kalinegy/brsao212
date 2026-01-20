quantidade_alunos = int(input("Quantos alunos há na turma? "))
soma_notas = 0

for i in range(quantidade_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma_notas += nota

media = soma_notas / quantidade_alunos

print("Média da turma:", round(media, 2))
