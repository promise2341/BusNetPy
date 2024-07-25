def find_cycle(sequence):
    n = len(sequence)
    for cycle_length in range(1, n // 2 + 1):
        cycle = sequence[:cycle_length]
        repeated = True
        for i in range(cycle_length, n, cycle_length):
            if sequence[i:i + cycle_length] != cycle:
                repeated = False
                break
        if repeated:
            return cycle
    return sequence