n = input('Введите строку арифметического выражения из однозначных чисел и знаков + и - : ')
res = int(n[0])
for i in range(1, len(n), 2):
    if n[i] == '+':
        res += int(n[i + 1])
    elif n[i] == '-':
        res -= int(n[i + 1])
print('Результат:', res)