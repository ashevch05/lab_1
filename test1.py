def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return (x * y) // gcd(x, y)


num1 = -12
num2 = 0

print("Числа:", num1, "і", num2)
print("НСД:", gcd(num1, num2))
print("НСК:", lcm(num1, num2))