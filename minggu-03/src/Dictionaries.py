tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel

#Konstruktor dict()membangun kamus langsung dari urutan pasangan nilai kunci:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

#Selain itu, pemahaman dict dapat digunakan untuk membuat kamus dari kunci arbitrer dan ekspresi nilai:
{x: x**2 for x in (2, 4, 6)}

#Jika kuncinya adalah string sederhana, terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci:
dict(sape=4139, guido=4127, jack=4098)