bri = set(['Бразилия', 'Россия', 'Индия'])
print('Индия' in bri)
print('США' in bri)

bric = bri.copy()
bric.add('Китай')
print(bric.issuperset(bri))

bri.remove('Россия')
print(bri & bric)
