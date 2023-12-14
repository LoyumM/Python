def has_merge_conflict(pull_requests)-> bool:
    lines = []
    for request in pull_requests:
        lines += list(range(request[0], request[1]+1))
    return len(set(lines)) != len(lines)

print(has_merge_conflict([[5, 10], [15, 40], [25, 50]]))