def is_triangle(a, b, c):

    if a + b > c and a + c > b and b + c > a:
        return True
    return False

sides = [(3, 4, 5), (1, 2, 3), (7, 10, 5)]

for a, b, c in sides:
    if is_triangle(a, b, c):
        print(f"{a}, {b}, and {c} can form a triangle.")
    else:
        print(f"{a}, {b}, and {c} cannot form a triangle.")
