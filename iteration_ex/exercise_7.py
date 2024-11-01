initial = int(input("Initial limit: "))
final = int(input("Final limit: "))

if initial == final:
    print(f"Sum of numbers from {initial} till {final}")
    print(initial)
elif initial > final:
    print(f"The initial limit must be smaller than the final limit")
else:
    print(f"Sum of numbers from {initial} till {final}")
    result = initial
    for i in range(initial + 1, final + 1):
        result += i
        print("+", i, "-->", result)


