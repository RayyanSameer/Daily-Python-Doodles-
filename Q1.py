#Manual Version

def remove_dupes_manually(nums):
    seen = []
    for num in nums:
        if num not in seen:
            seen.append(num)
    return seen

def remove_dupes_set(nums):
    seen = set()
    result = []
    for i in nums:
        if i not in seen:
            seen.add(i)
            result.append(i)

    return result                

print(remove_dupes_set([1, 3, 2, 3, 1, 4,7,8,8,9,87]))
print("Manual Version:", remove_dupes_manually([1, 3, 2, 5, 4, 3, 1, 4]))