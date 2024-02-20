texto = input('Informe um texto para verificacao de vogais: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:
    print()
    print('Executa no final do laco')
    
for numero in range(0, 51, 5):
    print(numero)
    
    