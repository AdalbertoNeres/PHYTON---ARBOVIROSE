from time import sleep
from datetime import date
print('\033[1m-=-'*10,'\033[1;32mUBV\033[m','\033[1m-=-\033[m'*10)
print('\033[1mAnálise de dados do Diário de UBV - Operadores')
print('Data {}'.format(date.today()))
print('')
kmini = int(input('Qual KM inicial? '))
kmfin = int(input('Qual KM final? '))
qt = int(input('Quantidade de Quarteirões: '))
calda = qt*120
km = kmfin-kmini
combvt=km/8
temp=int(input("Tempo da Jornada: "))
vazao = 0
while not vazao:
    if calda/temp <=71 or calda/temp >=76:
        temp=int(input('Tempo de Jornada inválido, informe novamente tempo de jornada: '))
    else:
        vazao=calda/temp
combleco = temp/60*4
sleep(1)
print('\033[1;32m-=-=\033[m'*10)
print('\033[1mTotal do KM :\033[1;33m{}km\033[m '.format(km))
print('\033[1mTotal da Calda:\033[1;33m{} Litros\033[m'.format(calda/1000))
print('\033[1mCombustivel da Viatura:\033[1;33m{:.2f} Litros\033[m'.format(combvt))
print('\033[1mCombustivel da LECO:\033[1;33m{:.2f} Litros\033[m'.format(combleco))
print('\033[1mTempo da Jornada:\033[1;33m {} minutos\033[m'.format(temp))
print('\033[1;40;31mVazão:{}\033[m'.format(vazao))



            
