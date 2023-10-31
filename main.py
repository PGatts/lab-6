# Param Gattupalli
# COP3502C Lab 6

# Juliana added the decode function

# Encode the password by adding 3 to each digit
def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_password += str((int(digit)+3) % 10)
    return encoded_password


def decode(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_password += str((int(digit)-3) % 10)
    return decoded_password


def main():
    choice, encoded_password = 0, ''
    while choice != 3:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Exit')
        choice = int(input("Please enter an option: "))

        # Perform operation depending on user choice
        match choice:
            case 1:
                password = input("Please enter your password to encode: ")
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            case 2:
                decoded_password = decode(encoded_password)
                print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
            case 3:
                exit()
            case _:
                print("Please select an option 1-3.")

if __name__ == '__main__':
    main()