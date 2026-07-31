class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_sorted = sorted(citations, reverse=True)
        ans = 0

        for ind, citation in enumerate(citations_sorted):
            if citation > ans and ind + 1 > ans:
                ans += 1
        return ans
