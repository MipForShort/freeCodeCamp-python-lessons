def dfs_n_queens(n: int):
    if n < 1:
        return []

    solutions = []
    stack = [[]]

    while stack:
        current_solution = stack.pop()

        if len(current_solution) == n:
            solutions.append(current_solution)
            continue
        
        row = len(current_solution)
        for col in range(n - 1, -1, -1):
            if is_safe(current_solution, row, col):
                stack.append(current_solution + [col])


    return solutions

def is_safe(current_solution, row, col):
    for r, c in enumerate(current_solution):
        if c == col or abs(c - col) ==  abs(r - row):
            return False
    
    return True