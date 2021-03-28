number = int(input('Введите трехзначное число: '))
reverse = (number % 10 * 100) + (number // 10 % 10 * 10) + (number // 100 % 10)
print(reverse)