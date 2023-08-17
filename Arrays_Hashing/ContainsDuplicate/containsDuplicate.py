# Time complexity -> O(n)
# Space Complexity -> unique_items + duplicates = O(n)
def main(arr):
    unique_items = set()
    duplicates = []
    for i in range(len(arr)):
        if arr[i] in unique_items:
            duplicates.append(arr[i])
        else:
            unique_items.add(arr[i])
    return duplicates

print(main([1,2,3,4,1,2]))

# neg-marking
# Time complexity -> O(n)
# Space Complexity -> O(1)

def neg_marking(arr):  # 1-n
    # [-1,-2,3,4,1]
    duplicates = []
    for i in range(len(arr)):
        index = abs(arr[i])-1
        if arr[index] < 0:
            duplicates.append(arr[index] * -1)
        else:
            arr[index] *= -1
    return duplicates

print(neg_marking([1,2,3,4,2,3]))

