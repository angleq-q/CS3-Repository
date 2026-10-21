numbers=[5,12,18,23,31,47,56,68,74,90]
target=47

def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

print(linear_search)