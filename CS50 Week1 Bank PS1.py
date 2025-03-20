'''In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20.
Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.'''

greeting = str(input("Please type a greeting."))

if greeting.strip().lower() == "hello":
    print("$0")
elif greeting.strip().lower().split()[0][0] == "h":
    #greeting.split()
    print("$20")
else:
    print("$100")

'''Run your program with python bank.py. Type Hello and press Enter. Your program should output:
$0 
Run your program with python bank.py. Type Hello, Newman and press Enter. Your program should output:
$0
Run your program with python bank.py. Type How you doing? and press Enter. Your program should output
$20
Run your program with python bank.py. Type What's happening? and press Enter. Your program should output
$100'''