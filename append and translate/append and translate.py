table = str.maketrans('abcdef','uvwxyz')
print(table)
print(chr(97),chr(117))
print('fad'.translate(table))
print('desktop'.translate(table))

students = []
students.append(['Demoines', 'Jim', 'Sophomore', 3.45])
students.append (['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append (['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edger', 'Junior', 3.99])
print((students))