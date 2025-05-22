def calculate_formula(x):
    result = x ** 3 - 5 * x + 1
    print(f"x = {x}, f(x) = {result}")
    return result

def next_value(a, b):
    fa = calculate_formula(a)
    fb = calculate_formula(b)
    return (a * fb - b * fa) / (fb - fa)

def main():
    iterations = 10
    x0 = 0
    x1 = 1

    print("\n")
    for i in range(1, iterations):
        print(f"Iterations {i}")
        print(f"x{i-1} = {x0}, x{i} = {x1}")

        next_x = next_value(x0, x1)
        result = calculate_formula(next_x)
        print(f"x{i+1} = {next_x}, f(x{i+1}) = {result}")

        x0 = x1
        x1 = next_x

        if x0 == x1:
            return x0

        if result == 0:
            return next_x

        if i == iterations - 1:
            return next_x

        print("\n")

print("Final Result", main())
