Nota1 = input('Digite a nota 1: ')
Nota2 = input('Digite a nota 2: ')

N1 = eval(Nota1)
N2 = eval(Nota2)

media = (0.4 * N1) + (0.6 * N2)

if media >= 5.0:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')
