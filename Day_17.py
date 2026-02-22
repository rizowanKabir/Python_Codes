# -----------------Pattern Problem------------------- #

# Square pattern problem
def square_pattern_problem(n):
    print("-----Square Star Pattern------")
    for i in range(n):
        print("* " * n )
    print()
square_pattern_problem(5)
# Inverted Pyramid Star Pattern
def inverted_pyramid_star_pattern(n):
    print("-----Inverted Pyramid Star Pattern-----")
    for i in range(n,0,-1):
        print(" " * (n-i) + "* " * i)
    print()
inverted_pyramid_star_pattern(5)
# Pyramid Star Pattern
def pyramid_star_pattern(n):
    print("------Pyramid Star Pattern------")
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)
    print()
pyramid_star_pattern(10)
# Diamond Star Pyramid
def diamond_star_pyramid(n):
    print("-----Diamond Star Pyramid-------")
    for i in range(1,n+1):
        print(" " * (n-i) + "* " * i)
    for i in range(n, 0, -1):
        print(" " * (n-i) + "* " * i)
    print()
diamond_star_pyramid(5)
# Hollow Square Star pattern
def hollow_square_star_pattern(n):
    print("-----Hollow Square Star Pattern-----")
    for i in range(n):
        if i == 0 or i == n-1:
            print("* " * n)
        else:
            print("* " + "  " * (n-2) + "*")
        print()
hollow_square_star_pattern(5)
# Butterfly Pattern
def butterfly_pattern(n):
    print("------Butterfly pattern------")
    for i in range(1, n+1):
        print("*" * i + " " * (2 * (n -i)) + "*" * i)
    for i in range(n, 0, -1):
        print("*" * i + " " * (2 * (n-i)) + "*" * i)
    print()
butterfly_pattern(7)
# Downward triangle Star pattern
def downward_triangle_star_pattern(n):
    print("--------Downward Triangle Star Pattern-----------")
    for i in range(n, 0, -1):
        print("* " * i)
    print()
downward_triangle_star_pattern(8)
# Hollow Diamond Star pattern
def hollow_diamond_star_pattern(n):
    print("-------Hollow Diamond Star Pattern----------")

    # Upper part
    for i in range(1, n + 1):
        if i == 1:
            print(" " * (n - i) + "*")
        else:
            print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")

    # Lower part
    for i in range(n - 1, 0, -1):
        if i == 1:
            print(" " * (n - i) + "*")
        else:
            print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")

    print()
hollow_diamond_star_pattern(10)

# Cross Star Pattern
def cross_star_pattern(n):
    print("------Cross Star Pattern------")
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if i == mid or j == mid:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print()
cross_star_pattern(7)
# Hollow Pyramid Star Pattern
def hollow_pyramid_star_pattern(n):
    print("--- Hollow Pyramid Star Pattern ---")
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print()
hollow_pyramid_star_pattern(10)

