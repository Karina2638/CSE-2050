word = 'fridge'
ins = input()

x = len(word)
y = 0

it = ''
while y < x:
    if ins[y:y+1] == word[y:y+1]:
        it = it + ins[y:y+1]
    else:
        it = it + '-'
    y += 1

print(it)