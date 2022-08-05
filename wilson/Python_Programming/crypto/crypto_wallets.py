import random
from RSA import *
from primes import *

get_users = input("Enter the number of users:\n")
users = int(get_users)

for i in range(users):
    get_key = random.randrange(len(primes_num))
    public_key = primes_num[get_key]
    private_key = find_private_key(public_key, carmichael)
    validate_public_key(public_key, carmichael)

    print("--------------------------------------------------------------------------------------------------------")
    name = input("Enter your name:\n")
    username = input("Create a username:\n")
    password = input("Create a password:\n")
    money = input("Account balance:\n")

    print("\n" + "------------------------------------")
    print("Your Keys")
    print("------------------------------------")

    if public_key == private_key:
        print("Sign Up Unsuccessful! Try Again!")
        quit()
    else:
        print("Public Key: " + str(public_key))
        print("Private Key: " + str(private_key) + "\n")

        with open('user' + str(i + 1) + '.txt', 'w') as file:
            file.write(name + "\n")
            file.write(username + "\n")
            file.write(password + "\n")
            file.write(str(public_key) + "\n")
            file.write(str(private_key) + "\n")
            file.write(str(money) + "\n")