import random

def partition(arr, left, right):
    pivot = arr[right]
    boundary = left - 1
    for index in range(left, right):
        if arr[index] <= pivot:
            boundary += 1
            arr[boundary], arr[index] = arr[index], arr[boundary]
    arr[boundary + 1], arr[right] = arr[right], arr[boundary + 1]
    return boundary + 1

def random_partition(arr, left, right):
    random_idx = random.randint(left, right)
    arr[random_idx], arr[right] = arr[right], arr[random_idx]
    return partition(arr, left, right)

def quick_select(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_idx = random_partition(arr, left, right)
    pivot_rank = pivot_idx - left + 1
    if k == pivot_rank:
        return arr[pivot_idx]
    elif k < pivot_rank:
        return quick_select(arr, left, pivot_idx - 1, k)
    else:
        return quick_select(arr, pivot_idx + 1, right, k - pivot_rank)

def median_of_groups(arr, left, right):
    if right - left < 5:
        return sorted(arr[left:right+1])[(right - left) // 2]
    medians = []
    for i in range(left, right + 1, 5):
        sub_list = sorted(arr[i:min(i+5, right+1)])
        medians.append(sub_list[len(sub_list) // 2])
    return deterministic_selection(medians, 0, len(medians)-1, len(medians)//2 + 1)

def deterministic_partition(arr, left, right, pivot):
    for i in range(left, right + 1):
        if arr[i] == pivot:
            arr[i], arr[right] = arr[right], arr[i]
            break
    return partition(arr, left, right)

def deterministic_selection(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot = median_of_groups(arr, left, right)
    pivot_idx = deterministic_partition(arr, left, right, pivot)
    pivot_rank = pivot_idx - left + 1
    if k == pivot_rank:
        return arr[pivot_idx]
    elif k < pivot_rank:
        return deterministic_selection(arr, left, pivot_idx - 1, k)
    else:
        return deterministic_selection(arr, pivot_idx + 1, right, k - pivot_rank)

# Example Usage
data_sample = [1,11,12,22,23,24,55,66,77,89]
k_value = 3
print(f"Quick Select ({k_value}th smallest):", quick_select(data_sample[:], 0, len(data_sample)-1, k_value))
print(f"Deterministic Select ({k_value}th smallest):", deterministic_selection(data_sample[:], 0, len(data_sample)-1, k_value))
