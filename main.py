# Param Gattupalli
# COP3502C Lab 6

def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_password += str((int(digit)+3) % 10)
    return encoded_password

def decode(encoded_password):
    pass

def main():
    choice = 0
    while choice != 3:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Exit')
        choice = int(input("Please enter an option: "))

        match choice:
            case 1:
                password = input("Please enter your password to encode: ")
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            case 2:
                decode(encoded_password)
            case 3:
                exit()

if __name__ == '__main__':
    main()