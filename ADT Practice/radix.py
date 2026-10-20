# Here we write a file to implement radix sorting
from typing import List
from collections import defaultdict



def bucket_sort(arr : List[int], d : int) -> List[int]:
    # arr is a list of integers
    ans = [[] for _ in range(10)]
    for num in arr:
        digit = (num // (10**d)) % 10
        ans[digit].append(num)

    return [item for sublist in ans for item in sublist] # flattened answer

def intital_bucketing(arr : List[int]) -> dict:
    # returns an list of lists where we sort into groups of i digits
    buckets = defaultdict(list)
    for num in arr:
        buckets[len(str(num))].append(num)
    return buckets

def radix_sort(arr : List[int], m):
    for d in range(0, m):
        arr = bucket_sort(arr, d)
    return arr

def main():
    arr = [456, 12, 9, 87, 1024, 3, 999]
    
    # 1. Group the numbers by length
    nums_by_length = intital_bucketing(arr)
    
    final_sorted_array = []
    
    # 2. Iterate through the lengths in sorted order (e.g., 1, 2, 3...)
    for length in sorted(nums_by_length.keys()):
        # 3. Sort the specific bucket using radix sort
        sorted_chunk = radix_sort(nums_by_length[length], length)
        
        # 4. Append the sorted chunk to the final answer
        final_sorted_array.extend(sorted_chunk)
        
    print(final_sorted_array)
    # Expected output: [3, 9, 12, 87, 456, 999, 1024]
main()