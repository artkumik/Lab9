def main():
    print(encode(12345555))

def encode(user):
    user = str(user)

    encoding_list = [3,4,5,6,7,8,9,1,2]
    encoded_user = ""

    for i in user:
        encoded_user = encoded_user + str(encoding_list[int(i)])

    return encoded_user

if __name__ == "__main__":
    main()