from user1 import *
from transfer_funds import *
from nft_ownership import *

print("-----------------------------------------------------")
print("User Login")
print("-----------------------------------------------------")

user_info = []
user_file = open("user2.txt", "r")

for i in user_file:
    data = i.replace("\n", "")
    user_info.append(data)

user_public_key = int(user_info[3])
user_private_key = int(user_info[4])
user_money = int(user_info[5])

# login
user_name = input("Name: ")
user_username = input("Username: ")
user_password = input("Password: ")

if user_name == user_info[0] and user_username == user_info[1] and user_password == user_info[2]:
    print("\n" + "--------------")
    print(user_name + "'s Account")
    print("--------------")
    print("Account Balance: " + str(user_money) + " coins")
    print("Public Key: " + str(user_public_key))
    print("\n" + "----------------------------------------------------------------------------------------------------")

    print("\n" + "What would you like to do?")
    print("a - Transfer Funds")
    print("b - Buy an NFT")
    to_do = input("Pick a option: ")

    if to_do == "a":
        transfer(user1_name, user1_money, user_name, user_money, user_private_key, user_public_key, 50)
    elif to_do == "b":
        transferOwnership(user1_money, user_money, user_name)
    else:
        print("No transactions in progress")
else:
    print("\n" + "Invalid Username/Password, try again!")
    quit()