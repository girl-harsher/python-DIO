produto_1 = 10
produto_2 = 20

print(produto_1+produto_2+3.5)
print(produto_1-produto_2)
print(produto_1/produto_2)
print(produto_1//produto_2)
print(produto_1*produto_2)
print(produto_1%produto_2)
print(produto_1**produto_2)

x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 2)
z = (10 / 2) + (25 * (2 - 2) ** 2)
print(x)
print(y)
print(z)

saldo = 500
saque = 200
print(saque > saldo)

adicao = 500
adicao += 200
print(saldo)

subtracao = 400
subtracao -= 100
print(subtracao)

multiplicacao = 700
multiplicacao *= 400
print(multiplicacao)

divisao = 700
divisao *= 400
print(divisao)

# operadores de comparação
# op_comparacao+op_logico+op_comparacao
# saldo >= saque and saque <= limite
# com o AND é necessário que as duas sejam verdadeiras senão teremos FALSE
# com o OR é necessário que somente uma seja TRUE, para ser FALSE as duas precisam ser falsas
# a precedencia de NOT antes da expressão inverte o valor booleano
not 1000 > 1500
# vai ser True
# uma lista vazia em python é considerada FALSE