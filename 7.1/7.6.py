#На вход программе подается натуральное число n. Напишите программу, которая для каждого из чисел от 0 до 
#n (ВКЛЮЧИТЕЛЬНО, ПОЭТОМУ n + 1) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).

n = int(input())
for i in range(n+1):
    print("Квадрат числа", i,"равен", i ** 2)