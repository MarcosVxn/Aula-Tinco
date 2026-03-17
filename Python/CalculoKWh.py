kwhReceber = int(input('Digite o KWh consumido: '))
print('1 - Residencia')
print('2 - Indústria')
print('3 - comércio')
tipoInstalação = int(input('Qual tipo de intalação: '))

if (tipoInstalação == 1 and kwhReceber <= 500):
    res = kwhReceber * 0.40
    print('valor a pagar {}'.format(res))
elif(tipoInstalação == 1 and kwhReceber > 500):
    res = kwhReceber * 0.65
    print('valor a pagar {}'.format(res))
    
if (tipoInstalação == 2 and kwhReceber <= 1000):
    res = kwhReceber * 0.55
    print('valor a pagar {}'.format(res))
elif (tipoInstalação == 2 and kwhReceber >1000):
    res = kwhReceber * 0.60
    print('valor a pagar {}'.format(res))
