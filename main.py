while True:
    name = input('Write your name here: ')
    if name.isalpha() and len(name) > 2:
        print(f'Your name is {name.capitalize()}')
        break
    else:
        print('Failed to initialize name. Try again.\n')