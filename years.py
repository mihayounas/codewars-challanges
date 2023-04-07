def solution(years):
    result = []
    
    for i in range(1, len(years)):
        total_time = 0
        travel_time = abs(years[i] - years[i-1])
        if years[i] == years[i-1]:
            total_time += 0
        elif years[i] > years[i-1]:
            total_time += 1
        else:
            total_time += 2
        result.append(total_time)
        
    return sum(result)
