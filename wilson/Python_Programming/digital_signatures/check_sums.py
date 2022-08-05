# uses check sums to verify messages

def byte_checksum(message):
    parity_byte = 0
    for c in message:
        parity_byte += ord(c)
        parity_byte = parity_byte % 256
    parity_byte = (~parity_byte + 1) % 256
    return message + chr(parity_byte)

def verify_byte(message):
    parity_check = 0
    for c in message:
        parity_check += ord(c)
        parity_check = parity_check % 256

    if parity_check == 0:
        print("Valid Checksum")
    else:
        print("Invalid Checksum")

# create msg
message1 = "Hello"
message2 = byte_checksum(message1)
print(message2)
verify_byte(message2)

new_msg = "HelloT"
print(new_msg)
verify_byte(new_msg)