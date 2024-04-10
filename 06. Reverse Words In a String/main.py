class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        return " ".join(lst[::-1])


sol = Solution()
s = "the sky is         blue"
print(sol.reverseWords(s))