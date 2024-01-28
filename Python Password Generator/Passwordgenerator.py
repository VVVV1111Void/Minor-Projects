import random
import string

def Ask():
    answers = {
        'len' : 0,
        'mlen' : 0,
        'Mlen' : 0,
        'ammount' : 1
    }

    answers['len'] = (input('Input a integer length (0 for random)\n'))
    if (str(answers['len'])).lower() == 'exit':
        return 0

    answers['ammount'] = (input('How many passwords?\n'))
    if (str(answers['ammount'])).lower() == 'exit':
        return 0

    if answers['len'] != 0:
        return answers

    answers['Mlen'] = (input('Input a integer max length (0 for none)\n'))
    if (str(answers['Mlen'])).lower() == 'exit':
        return 0

    answers['mlen'] = (input('Input a integer min length (0 for none)\n'))
    if (str(answers['mlen'])).lower() == 'exit':
        return 0

    
    for inp in answers:
        answers[inp] = int(answers[inp])
    return answers
    print('Error!')
    Ask()


def Password(n) -> str:
    chars = list(string.ascii_letters + string.digits + string.punctuation)
    passwords = []
    random.shuffle(chars)

    for p in range(0, int(n['ammount'])):
        password = []
        if n['len'] != 0:
            while len(password) < int(n['len']):
                password.append(random.choice(chars))
                random.shuffle(password) 
            while len(password) > int(n['len']):
                password.pop(-1)
                random.shuffle(password) 

        if n['len'] == 0:
            number = random.randint(0, 15)
            for i in range(0, number + 1):
                password.append(random.choice(chars))
                random.shuffle(password)

        if n['mlen'] != 0:
            while len(password) < int(n['mlen']):
                password.append(random.choice(chars))
                random.shuffle(password)

        if n['Mlen'] != 0:
            while len(password) > int(n['Mlen']):
                password.pop(-1)
                random.shuffle(password)
                
        passwords.append(str("".join(password)))
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