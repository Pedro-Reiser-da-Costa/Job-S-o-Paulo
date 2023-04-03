num = 13

fib = [0, 1]

while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

if num in fib:
    print(f'O número {num} pertence à sequência de Fibonacci.')
else:
    print(f'O número {num} não pertence à sequência de Fibonacci.')





import json

with open('faturamento.json') as f:
    faturamento_diario = json.load(f)

faturamento_diario = [float(f) for f in faturamento_diario]

faturamento_diario = [f for f in faturamento_diario if f != 0]

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_media = 0
for f in faturamento_diario:
    if f > media_mensal:
        dias_acima_media += 1

print(f"Menor faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")





faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())

percentuais = {}
for estado, faturamento in faturamento_por_estado.items():
    percentuais[estado] = (faturamento / faturamento_total) * 100

for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')





string = input('Digite uma string: ')

caracteres = list(string)

i = 0
j = len(caracteres) - 1
while i < j:
    caracteres[i], caracteres[j] = caracteres[j], caracteres[i]
    i += 1
    j -= 1

string_invertida = ''.join(caracteres)

print('String invertida:', string_invertida)
