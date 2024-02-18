opcao = int(input('Informe uma opção: [1] Sacar \n[2] Extrato: '))

if opcao == 1:
    valor = float(input('Informe a quantia para o saque: '))
elif opcao == 2:
    print('Exibindo extrato...')
else:
conta_normal = True
conta_universitaria = False
saldo = 2000
cheque_especial = 450    
    
saque = (int(input('Insira o valor para saque: ')))
if saldo >= saque:
        print('Saque realizado com sucesso!')
        
elif saque <= (saldo+cheque_especial):
        print('Saque realizado com uso do cheque especial!')
        
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
        
else:
        print('Saldo insuficiente')
        
status = 'Sucesso' if saldo >=saque else 'Falha'
print(f'{status} ao realizar o saque!')