def merge_sorted_lists(listA: list, listB: list) -> list:
    return sorted(listA + listB)

listA = [1, 5, 6, 7, -1, 91, 56]
listB = [2, 4, 3, 7, -2, 56, 51]

print(merge_sorted_lists(listA, listB))