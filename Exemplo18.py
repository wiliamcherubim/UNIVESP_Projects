"""
A = input("Digite o algoritmo A: ")
A1 = eval(A)
B = input("Digite o algoritmo B: ")
B1 = eval(B)
C = input("Digite o algoritmo C: ")
C1 = eval(C)
D = input("Digite o algoritmo D: ")
D1 = eval(D) """
linha = input().split()
A, B, C, D = list(map(int, linha))

if (B > C) and (D > A) and ((C+D) > (A+B)) and (C > 0 and D > 0) and (A % 2) == 0:
                print("Valores aceitos")
else:
    print("Valores não aceitos")

