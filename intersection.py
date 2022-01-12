def intersect(set1,set2):
    result_set = set()
    for item in set1:
        if item in set2: 
            result_set.add(item)
    return result_set 