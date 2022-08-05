def prime_test(num):
    divisor = 2
    if num <= 2:
        print("You need to choose a number higher than 2 bc im lazy")
        return
    while divisor != num:
        if (num % divisor) == 0:
            print("Not prime")
            return
        divisor += 1
    print("is prime")

number = int(input("input number"))
prime_test(number)