n = int(input('введите целое число: '))
number = 2
power = 1
while number <= n:
    number *= 2
    power += 1
print(power - 1, number // 2)