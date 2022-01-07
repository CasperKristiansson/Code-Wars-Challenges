def sum_of_intervals(intervals):
    offset = abs(min(map(min, intervals)))  
    counts = [0 for _ in range(max(map(max, intervals)) + offset)]
    
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            counts[i + offset] = 1

    return sum(counts)