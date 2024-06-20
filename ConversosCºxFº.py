# Função Converter Celsius para Fahrenheit
def CxF(c):
    f = c * 1.8 + 32
        print(f'{c} Cº em Fahrenheit fica: {f:.1f} Fº')


# Função Converter Fahrenheit para Celsius
def FxC(f):
    c = (f - 32) / 1.8
    print(f'{f} Fº em Celsius fica: {c:.1f} Cº')


# Solicitação de Informações
while True:
    Conversao = input('Gostaria de transformar para Celsius ou Fahrenheit? (c/f) ')
    if Conversao.lower() == 'c':
        Grau = float(input('Digite a temperatura: '))
        FxC(Grau)
        Replay = input('Deseja continuar? (s/n) ')
        if Replay.lower() == 's':
            print('')
        else:
            break
    elif Conversao.lower() == 'f':
        Grau = float(input('Digite a temperatura: '))
        CxF(Grau)
        Replay = input('Deseja continuar? (s/n) ')
        if Replay.lower() == 's':
            print('')
        else:
            break
    else:
        print('Formato inválido')

print('Acabou, obrigado')
