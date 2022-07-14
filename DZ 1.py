# Первый вариант:
n = input("Введите число: ")
n = int(n)
 
sum = 0
mult = 1
 
while n > 0:
    digit = n % 10
    sum = sum + digit
    mult = mult * digit
    n = n // 10
 
print("Сумма:", sum)

# Второй вариант:

n = input("Введите число: ")
n = int(n)

d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100

print("Сумма:", d1 + d2 + d3)
