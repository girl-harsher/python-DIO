curso = 'curso de python'
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
curso is not nome_curso
curso is limite

saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)