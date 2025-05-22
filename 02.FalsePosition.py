def calculate_formula(x):
    result = x ** 3 - 3 * x + 1
    print(f"x = {x}, f(x) = {result}")
    return result

def next_value(a, b):
    fa = calculate_formula(a)
    fb = calculate_formula(b)
    return (a * fb - b * fa) / (fb - fa)

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
        print(f"Iterations {i + 1}")
        avg = next_value(a, b)
        result = calculate_formula(avg)
        if result < 0:
            a = avg
        elif result > 0:
            b = avg
        else:
            return avg
        print("\n")

    return next_value(a, b)

print("Final Result", main())
