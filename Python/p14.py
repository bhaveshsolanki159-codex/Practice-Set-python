def solve_puzzle(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens  
        if (2 * chickens + 4 * rabbits) == legs:
            print(chickens, rabbits)
            return
    print("No solution")

test_cases = [(35, 94), (150, 400), (3, 11), (3, 12), (5, 10)]
for heads, legs in test_cases:
    print(f"heads-{heads} legs-{legs}")
    solve_puzzle(heads, legs)
