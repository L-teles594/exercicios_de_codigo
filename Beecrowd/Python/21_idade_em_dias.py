# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
#
# Obs.: apenas para facilitar o cálculo, considere todos anos com 365 dias e todos mêses com 30 dias. Nos casos de teste
#  nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com
#  objetivo de testar raciocínio matemático simples.
#
# Entrada
# O arquivo de entrada contém um valor inteiro.
#
# Saída
# Imprima a saída conforme exemplo fornecido.
idade_em_dias = int(input())

conversores = [365, 30]

for conversor in conversores:
    contador = 0

    while idade_em_dias >= conversor:
        idade_em_dias -= conversor
        contador += 1

    if conversor == 365:
        print(f'{contador} ano(s)')
    elif conversor == 30:
        print(f'{contador} mes(es)')

print(f'{idade_em_dias} dia(s)')