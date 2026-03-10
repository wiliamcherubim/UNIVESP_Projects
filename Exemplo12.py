acum = 0
for x in range(1, 101):
    if x % 2 == 0:
        acum = acum + x
print(acum, '\n')

# Exercício 2

str_list = ['Joao', 'Roberto', 'Rafael']

for nome in str_list:
    for c in nome:
        if c in 'aeiou':
            print(c)