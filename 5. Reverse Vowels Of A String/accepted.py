class Solution:
    def reverseVowels(self, s: str) -> str:
        st = list(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(st) - 1
        # print(vowels)

        while left < right:
            while left < right and st[left].lower() not in vowels:
                left += 1
            while left < right and st[right].lower() not in vowels:
                right -= 1
            

            st[left], st[right] = st[right], st[left]
            left += 1
            right -= 1
        return "".join(st)

solution = Solution()
s = "hello"
print(solution.reverseVowels(s))