# generates unique non-fungible tokens (NFT's)
import string
import random

def nft_token():
    token = ""
    letter = string.ascii_lowercase
    numbers = string.digits
    for i in range(30):
        token += ''.join(random.choice(letter + numbers))
    return token

#print(nft_token())

