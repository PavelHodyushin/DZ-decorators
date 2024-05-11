
def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res > 1:
            print("Простое")
        elif res == 1:
            print("Число 1 не является ни простым, ни составным числом")
        else:
            print("Составное")
        return res
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2,3,6)
print(result)
result = sum_three(0,1,0)
print(result)
result = sum_three(-1,0,0)
print(result)