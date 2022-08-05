# checks if num is prime, creates prime pairs for RSA algorithm
p_nums = []
q_nums = []

def isPrime(n: int):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    k = 5
    while k ** 2 <= n:
        if n % k == 0 or n % (k + 2) == 0:
            return False
        k += 6
    return True

#print(isPrime(81))

primes_num = []
for i in range(128, 512):
    if isPrime(i):
        primes_num.append(i)
#print(primes_num)

# find primes work well with RSA
for i in primes_num:
    for x in range(1, 5):
        check = i * x + 1
        if primes_num.count(check) == 1:
            #print("For: " + str(i) + " q:" + str(check))
            p_nums.append(i)
            q_nums.append(check)

length = 0
if len(p_nums) == len(q_nums):
    length = len(q_nums)