class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # takes 2 lists in sorted order and returns a master list in sorted order
        def merge(l1, l2):
            p1, p2 = 0, 0
            ans = []
            while p1 < len(l1) or p2 < len(l2):
                if p1 < len(l1) and p2 < len(l2):
                    if l1[p1] <= l2[p2]:
                        ans.append(l1[p1])
                        p1 += 1
                    else:
                        ans.append(l2[p2])
                        p2 += 1

                elif p1 < len(l1):
                    ans.append(l1[p1])
                    p1 += 1
                else:
                    ans.append(l2[p2])
                    p2 += 1
            return ans

        def mergeSort(lst : List[int]):
            if len(lst) == 1:
                return lst
            else:
                m = len(lst) // 2
                return merge(mergeSort(lst[ : m]), mergeSort(lst[m: ]))


        return mergeSort(nums)