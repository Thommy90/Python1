students1 = int(input('Введите количество школьников в 1 математическом классе: '))
students2 = int(input('Введите количество школьников в 2 математическом классе: '))
students3 = int(input('Введите количество школьников в 3 математическом классе: '))
class1 = (students1 // 2) + (students1 % 2)
class2 = (students2 // 2) + (students2 % 2)
class3 = (students3 // 2) + (students3 % 2)
desk = class1 + class2 + class3
print(desk, 'требуется закупить парт')