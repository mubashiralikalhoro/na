def calculate_formula(x):
    result = x ** 3 - 2 * x - 5
    print(f"x = {x}, f(x) = {result}")
    return result

def average(a, b):
    print(f"a = {a}, b = {b}")
    return (a + b) / 2

def main():
    iterations = 10
    a = -1
    b = -1
    i = 0

    # finding initial values
    while True:
        value = calculate_formula(i)
        if value < 0:
            a = i
        elif value > 0:
            b = i
        else:
            return value

        if a != -1 and b != -1:
            break

        i += 1

    print("\n")
    for i in range(iterations):
        avg = average(a, b)
        result = calculate_formula(avg)
        if result < 0:
            a = avg
        elif result > 0:
            b = avg
        else:
            return avg
        print("\n")

    return average(a, b)

print("Final Result", main())
