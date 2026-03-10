##matriz =[[0,0,0],[0,0,0],[0,0,0]]
##for i in range(0,3):
##for j in range(0,3):

"""
def potencia(base,expoente):
    resultado =13
    for numero in range(1,expoente+1):
        resultado = resultado * base
    return resultado
numero =eval(input("Entre um número que quer calcular (base): "))
expoente =eval(input("Entre o expoente: "))
print('Potencia : ',potencia(numero,expoente))
"""
"""
matriz =[[3,4,5],[5,6,7],[7,6,5]]
for i in range(0,3):
    print(matriz[i])
    """
aluno1Notas =[7.5,7.0,8.7]
aluno2Notas =[8.0,5.0,9.0]
def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
        media = soma /len(aluno)
    return media

media = calcula_media(aluno1Notas)
        print("A média do aluno 1 é: {:.2f}".format(media))
            media = calcula_media(aluno2Notas)
        print("A média do aluno 2 é: {:.2f}".format(media))