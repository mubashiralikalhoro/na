def fx(x):
    return x**3 - 3 * x - 5

def fx_(x):
    return 3 * x**2 - 3

def next_x(x):
    f = fx(x)
    f_ = fx_(x)
    return x - f / f_

def main():
    iterations = 10
    x = 2

    print("\n")
    for i in range(iterations):
        print("Iterations ", i + 1)
        if fx(x) == 0:
            return x
        
        new_x = next_x(x)
        print(f"x{i + 1} = {new_x}, f(x{i + 1}) = {fx(new_x)}")

        x = new_x

        if fx(x) == 0:
            return x

        if i == iterations - 1:
            return x

        print("\n")

print("Final Result", main())
