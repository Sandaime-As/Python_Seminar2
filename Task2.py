# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n=int(input('Введите число N: '))
index=1
mult_list=[]
for i in range(n):
    if i<=n:
        i=i*index
        index+=int(i)
    mult_list.append(index)
print(index, end=' ')
print()
print(mult_list)