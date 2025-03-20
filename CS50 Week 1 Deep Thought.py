'''In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.'''

forty_two = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?"))

if forty_two == ('42'):
    print('Yes')
elif forty_two == ('forty-two'):
    print('Yes')
elif forty_two == ('forty two'):
    print('Yes')
elif forty_two == ('forty_two'):
    print('Yes')
else:
    print('No')
