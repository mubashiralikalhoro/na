def next_values(x, y, z):
    next_x = (85 - 6 * y + z) / 27
    next_y = (72 - 6 * x - 2 * z) / 15
    next_z = (110 - x - y) / 54
    
    return {
        'x': next_x,
        'y': next_y,
        'z': next_z
    }

def main():
    iterations = 10
    x = 0
    y = 0
    z = 0
    
    for i in range(iterations):
        print(f"x{i} = {x}, y{i} = {y}, z{i} = {z}")
        next = next_values(x, y, z)
        x = next['x']
        y = next['y']
        z = next['z']

    print(f"x{iterations} = {x}, y{iterations} = {y}, z{iterations} = {z}")

main()
