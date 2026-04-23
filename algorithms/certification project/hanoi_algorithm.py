def hanoi_solver(n):
    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    
    states = []

    def save_state():
        state_str = f"{rods['A']} {rods['B']} {rods['C']}"
        states.append(state_str)

    def move(n, source, target, auxiliary):
        if n > 0:
            move(n - 1, source, auxiliary, target)
            
            disk = rods[source].pop()
            rods[target].append(disk)
            save_state()
            
            move(n - 1, auxiliary, target, source)

    save_state()
    move(n, 'A', 'C', 'B')
    
    return "\n".join(states)

if __name__ == '__main__':
    hanoi_solver(2)