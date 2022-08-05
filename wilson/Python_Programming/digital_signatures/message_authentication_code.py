# checks if message is valid by using digital signatures (MAC)

def sign_message(message, key):
    message_int = 0

    for c in message:
        message_int += ord(c)
    a = key[0]
    b = key[1]
    mac_tag = (a * message_int + b) % p
    return mac_tag

# public info
# p should be a prime number
p = 491
message = "Hello World"

# private info
# the numbers for key should be 0 < key < p
key = [15, 20]

# message is broadcast alongside its MAC
mac = sign_message(message, key)

def check_mac(old_mac, new_mac):
    if old_mac == new_mac:
        print("Message is valid")
    else:
        print("Message is compromised")

# recipient checks messages received
message1 = "Hello World"
message2 = "Hello World!"

# verify 1st msg
mac1 = sign_message(message1, key)
check_mac(mac, mac1)

# verify 2nd msg
mac2 = sign_message(message2, key)
check_mac(mac, mac2)