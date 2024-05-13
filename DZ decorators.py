def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n <= 1:
            print("Не простое")
            return n
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print("Составное")
                return n
        print("Простое")
        return n
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2,3,6)
print(result)
result = sum_three(3,3,3)
print(result)
result = sum_three(25,36,46)
print(result)
result = sum_three(43,78,21)
print(result)
result = sum_three(900,80,3)
print(result)
