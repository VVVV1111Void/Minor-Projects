import random
import string

def Ask():
    while True:
        answers = {
            'Length': int(input('Input a integer length (0 for random)\n') or '0'),
            'Amount': int(input('How many passwords?\n') or '1'),
            'Mlen': int(input('Input a integer max length (0 for none)\n') or '0'),
            'mlen': int(input('Input a integer min length (0 for none)\n') or '0')
        }
        
        if 'exit' in [str(val).lower() for val in answers.values()]:
            return 0
        
        return answers


def Password(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    passwords = []

    for _ in range(n['Amount']):
        password = []

        if n['Length'] > 0 :
            password = random.choices(chars, k=n['len'])
        elif n['mlen'] > 0:
            password = random.choices(chars, k=random.randint(n['mlen'], n['Mlen'] + 1))
        else:
            number = random.randint(0, 15)
            password = random.choices(chars, k=number)

        passwords.append(''.join(password)) # convert to string

    return passwords

if __name__ == "__main__":
    print('Welcome to my python password generator')
    print('Put "exit" anywhere to exit')
    n = Ask()
    if n != 0:
        print('Generating Password.')
        print(f'The password/s is/are: \n{str(Password(n))}')
    else:
        print('Okay Bye!')