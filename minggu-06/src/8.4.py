raise NameError('HiThere')



raise ValueError  # shorthand for 'raise ValueError()'



try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise