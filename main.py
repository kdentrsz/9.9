n = int(input('Сколько оценок вы хотите ввести? '))
k = 0
sum = 0
for i in range(n):
  m = int(input())
  k += 1
  sum += m
if 9<m<100:
  sr = sum/k
print('Их среднее арифметическое составляет',sr)

