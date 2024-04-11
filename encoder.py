def main():
    print(encode(12345555))
    print(decode('45678888'))

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