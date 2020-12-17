import random

n=int(input('Введите N: '))

a=[]

for i in range(n):#создание пустого массива
    a.append(0)

for j in range(n):#заполнение массива
    t=1
    while(t!=0):#генерация случайного числа с проверкой на повторение
        t=0
        p=random.randint(1,n)
        for i in range(n):
            if a[i]==p:
                t=1
    a[j]=p
    print(p)
    f=input("нажмите Enter")#заглушка

print(a)

f=input("нажмите Enter")#заглушка