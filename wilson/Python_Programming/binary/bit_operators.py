# logic gates

# and
A = 0b1101
B = 0b1010
C = A & B
print(bin(C))
# or
D = A | B
print(bin(D))
# not
E = ~A
print(bin(E))
# xor
F = A ^ B
print(bin(F))
# bit shifting
G = A << 1
H = A >> 2
I = A << 2
print(bin(G))
print(bin(H))
print(bin(I))