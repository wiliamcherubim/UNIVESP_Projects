C = input("Digite a temperatura em graus celsius: ")
# é necessário tranformar String em Int um vez
# que input entende como String
c_temp = eval(C)
print("A temperatura em graus célsius é: ", c_temp)
F = (1.8 * c_temp) + 32
print("A temperatura em Fahrenheit é: ", F)