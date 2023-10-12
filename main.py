while True:
    name = input('Write your name here: ')
    age = input('Write your age here: ')
    if (name.isalpha() and len(name) > 2) and (age.isdigit() and 5 < int(age) < 100):
        print(f'Your name is {name.capitalize()} and you are {age} years old')
        print('line')
        input('Press enter to exit')
        break
    elif not (name.isalpha() and len(name) > 2):
        print('Failed to initialize name\n')
    elif not (age.isdigit() and 5 < int(age) < 100):
        print('Failed to initialize age\n')