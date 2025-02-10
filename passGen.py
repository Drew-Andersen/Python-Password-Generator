import random
import string

def generator():
    length_pass = int(input('Enter the desired length of the password: '))
    include_uppercase = input('Would you like there to be uppercase letters (yes/no)? ').strip()
    include_lowercase = input('Would you like there to be lowercase letters (yes/no)? ').strip()
    include_special = input('Would you like there to be special characters (yes/no)? ').strip()
    include_digits = input('Would you like there to be numbers (yes/no)? ').strip()

    if length_pass < 5:
        print('The password needs to be at least 5 characters long.')
        return
    
    upper = string.ascii_uppercase if include_uppercase == 'yes' else ''
    lower = string.ascii_lowercase if include_lowercase == 'yes' else ''
    special = string.punctuation if include_special == 'yes' else ''
    digits = string.digits if include_digits == 'yes' else ''

    all_characters = upper + lower + special + digits

    required_chr = []
    if include_uppercase == 'yes':
        required_chr.append(random.choice(upper))
    if include_lowercase == 'yes':
        required_chr.append(random.choice(lower))
    if include_special == 'yes':
        required_chr.append(random.choice(special))
    if include_digits == 'yes':
        required_chr.append(random.choice(digits))

    remaining_chrs = length_pass - len(required_chr)
    password = required_chr

    for _ in range(remaining_chrs):
        char = random.choice(all_characters)
        password.append(char)

    random.shuffle(password)
    gen_password = ''.join(password)
    print('Password: ', gen_password)

generator()