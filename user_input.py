def reverse(text):
    return text[::-1]

def is_palindrome(text):
    punctuations = ['.', '?', '!', ':', ';', '-', '(', ')', '[', ']', '...', "'", '"', '/', ',', ' ']

    for p in punctuations:
        text = text.replace(p, '')        

    text = text.lower()
    return text == reverse(text)

something = input('Введите текст: ')

if (is_palindrome(something)):
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')