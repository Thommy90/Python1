students1 = int(input('Введите количество школьников в 1 математическом классе: '))
students2 = int(input('Введите количество школьников в 2 математическом классе: '))
students3 = int(input('Введите количество школьников в 3 математическом классе: '))
studentsall = students1+students2+students3
desk = (studentsall // 2) + (studentsall % 2)
print(desk, 'требуется закупить парт')