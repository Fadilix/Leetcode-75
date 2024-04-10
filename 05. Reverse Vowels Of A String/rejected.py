class Solution:
    def reverseVowels(self, s: str) -> str:
        st = [char for char in s]
        vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
        left, right = 0, len(s) - 1

        while right - left > 1:
            if st[left] not in vowels:
                left += 1
            if st[right] not in vowels:
                right -= 1
            if len(s) == 2:
                if st[left].lower() == st[right].lower():
                    left += 1
                    right -= 1
                else:
                    st[left], st[right] = st[left], st[right]
                    left += 1
                    right -= 1

            if st[left] in vowels and st[right] in vowels:
                st[left], st[right] = st[right], st[left]
                left += 1
                right -= 1

        return "".join(st)


solution = Solution()
s = "hello"
print(solution.reverseVowels(s))
