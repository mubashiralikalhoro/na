def next_values(x, y, z):
    next_x = (1 + y - z) / 3
    next_y = (-3 * next_x - 2 * z) / 6
    next_z = (4 - 3 * next_x - 3 * next_y) / 7
    return [next_x, next_y, next_z]


def display(i, places, x, y, z):
    str = f"x{i} = {round(x,places)}\ty{i} = {(round(y,places))}\tz{i} = {round(z,places)}"
    print(str)


def isSame(places, x, y, z, next_x, next_y, next_z):
    return (
        round(x, places) == round(next_x, places)
        and round(y, places) == round(next_y, places)
        and round(z, places) == round(next_z, places)
    )


def main():
    decimal_places = 11
    max_iterations = 20
    x, y, z = 0, 0, 0
    i = 0

    for i in range(max_iterations):
        display(i, decimal_places, x, y, z)
        next = next_values(x, y, z)

        if isSame(decimal_places, x, y, z, next[0], next[1], next[2]):
            print(f"\nSolved in {i + 1} iterations")
            break

        x, y, z = next

    display(i + 1, decimal_places, x, y, z)


main()
