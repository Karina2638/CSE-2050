# 1
print('Kia Smith is inviting you\nto a video meeting.\nJoin meeting:\nhttp://www.zoomskype.us/5592\nPhone:\n1-669-555-2634 (San Jose)\n1-929-555-4000 (New York)\nMeeting ID: 5592\n-------------------------\nReminder: 10 min before')

# 2
print('')
a = int(input('a: '))
b = int(input('b: '))
print(f'a^2: {a**2}')
print(f'b^2: {b**2}')
print(f'c^2: {a**2 + b**2}')

# 3
# script 1:
a = 36
b = 48
c = a + b
d = int(a) + b
e = a + b
# script 2:
my_school = 'UConn'
my_degree = 'Engineering'
my_name = 'Karina'
my_program = my_school + ' ' + my_degree
print('My name is ', my_name)
my_year = 1
print(f'I am attending {my_school} studying {my_program} and I am in my {my_year}st year\n')

# 4
one = int(input('number: '))
op = input('operation: ')
two = int(input('number: '))
if op == '+':
    print(f'{one} + {two} = {one + two}')
if op == '-':
    print(f'{one} - {two} = {one - two}')
if op == '*':
    print(f'{one} * {two} = {one * two}')
if op == '/':
    print(f'{one} / {two} = {one / two}')
if op == '%':
    print(f'{one} % {two} = {one % two}')
if op == '**' or op == '^':
    print(f'{one} ^ {two} = {one ** two}')
if op == '//':
    print(f'{one} // {two} = {one // two}')

# 5
print('')
og = int(input('price: '))
dis = input('discount: ')
print(f'{og} when {dis}% off is {(og * (1-float(dis)/100)):.2f}')