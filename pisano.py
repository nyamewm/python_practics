def pisano_period(m):
    a, b = 0, 1
    period = 0
    for _ in range(m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            period = _ + 1
            break
    return period

def fib_mod(n, m):
    pisano = pisano_period(m)
    remainder = n % pisano

    fib = [0, 1]
    for i in range(2, remainder + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % m)

    return fib[remainder]

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()