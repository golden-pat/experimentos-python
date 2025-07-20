while True:
    entrada = input("Quantos alunos fizeram a prova: ")
    if entrada.isdigit():
        numero = int(entrada)
        break
    else:
        print("Não tem como ter uma quantidade não numérica ou quebrada de alunos!")

notas = []

for i in range (1, numero+1):
    while True:
        nota = float(input(f"Digite a nota do aluno #{i}:"))
        notas.append(nota)
        break
    i+=1

for i in range (1, numero + 1):
    print(f"A nota do aluno #{i} é {notas[i - 1]}")
    i+=1

media = sum(notas)/len(notas)

print(f"A média da sala foi de {media:.2f}")