def main():
    while True:
        for i in range (0,12):
            print('-',end='')
        print('\n1. Encode')
        print('2. Decode')
        print('3. Quit')
        c = int(input('\nPlease enter an option: '))
        if c == 1:
            number = input("Please enter the number to encode: ")
            print(f"Your encoded number is {encode(number)}")
        elif c == 2:
            number = input("Please enter the number to decode: ")
            print(f"Your decoded number is {decode(number)}")
        elif c == 3:
            print('Goodbye!')
            break
        else:
            print("Please enter a valid option.")

def encode(user):
    user = str(user)

    encoding_list = [3,4,5,6,7,8,9,1,2]
    encoded_user = ""

    for i in user:
        encoded_user = encoded_user + str(encoding_list[int(i)])

    return encoded_user

def decode(encoded_user):
    lis = list(encoded_user)
    decoded_user = ''
    for i in range(len(lis)):
        lis[i] = int(lis[i])
        lis[i] = (lis[i] - 3) % 10
    for i in range(len(lis)):
        lis[i] = str(lis[i])
        decoded_user += ''.join(lis[i])
    return decoded_user

if __name__ == "__main__":
    main()