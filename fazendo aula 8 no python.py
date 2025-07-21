#Não sei se esse import os e o clear_screen estão funcionando pq a IDE (programiz.com) não deixa funções com OS funcionar por motivos de segurança, pra evitar isso tem que colocar um código ASCII que não é certeza que vai funcionar em todos OS (MacOS, Linux ou Windows)

import os

def clear_screen():
    if os.name == 'nt':
        cmd = 'cls'
    else:
        cmd = 'clear'
    os.system(cmd)

entrada = input ("Quantos alunos tem na sala:")
if entrada.isdigit():
    alunos = int(entrada)
else:
    print("Pessoas só tem como ser número inteiro!")
    
notas1 = []
notas2 = []

for i in range (1, alunos+1):
    while True:
        entrada = input (f"Diga a nota do {i}° aluno no primeiro bimestre:")
        try:
            entrada.isdigit()
            nota1 = float(entrada)
            notas1.append(nota1)
            break
        except ValueError:
            print("As notas só podem ser números!")
    i+=1

for i in range (1, alunos+1):
    while True:
        entrada = input (f"Diga a nota do {i}° aluno no segundo bimestre:")
        try:
            entrada.isdigit()
            nota2 = float(entrada)
            notas2.append(nota2)
            break
        except ValueError:
            print("As notas só podem ser números!")
    i+=1
    
clear_screen()
    
medfin = [(n1 + n2) / 2 for n1, n2 in zip(notas1, notas2)] #zip agrupa pares, então notas1= [10;90;73;…] e notas2= [90;23;12;…] ele vai pegar o primeiro de ambas as listas e juntar como um só, transformando notas1[1] e notas2[1] em n1 e n2
medtur = sum(medfin)/len(medfin)
    
for idx, (n1, n2, m) in enumerate(zip(notas1, notas2, medfin), start = 1): #transforma cada valor em triozinho que nem o de cima:    
 print (f"A nota do {idx}º aluno no 1º bimestre foi {n1:.1f} e no 2ª semestre foi {n2:.1f}, então a média dele é de {m:.2f}")
 print (f"Além disso, a média da turma foi {medtur:.2f}")
  

#Original era:
# #include <stdio.h>float notas[n];
# int main(){

#    int i=1,n;

#    printf("Quantos alunos tem na sala?\n");
#    scanf("%d", &n);
#
#    float notas1[n],notas2[n];
#
#    for (i;i<=n;i++){
#
#        printf("\nDigite a nota do %d° aluno no 1° bimestre:", i);
#        scanf("%f",&notas1[i]);
#   }
#
#       for (i=1;i<=n;i++){
#
#        printf("\nDigite a nota do %d° aluno no 2° bimestre:", i);
#        scanf("%f",&notas2[i]);
#   }
#
#
#   system("clear");
#
#   for (i=1;i<=n;i++){
#
#       printf("A nota do %d° aluno:\n1°Bim.: %.1f\n2° Bim.:%.1f\nMédia: %.1f\n\n", i, notas1[i], notas2[i], ((notas1[i]+notas2[i])/2));
#
#   }
#
#
#
#    return 0;
#}
