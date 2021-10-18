def int_func(txt):
    word = txt[0].upper() + txt[1:].lower()
    return word


text = input('enter words separated by space: ')
for word in text.split(' '):
    print(f'{int_func(word)}', end=' ')
