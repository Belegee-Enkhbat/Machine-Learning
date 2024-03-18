# 5. Хамгийн эхний анхны 50 тоог олох функц бич.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n+1)/2)):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

print(get_primes(50))


