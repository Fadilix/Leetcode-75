class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        Calculate the greatest common divisor (GCD) of two strings.
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # Define a recursive function to compute the GCD
        # This could be replaced with the built-in math.gcd() function
        # However, a custom implementation is used due to specific requirements
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        # Check if str1 + str2 forms a palindrome
        if str1 + str2 != str2 + str1:
            return ""
        
        # Calculate the GCD of the lengths of str1 and str2
        # Return the substring of str1 up to the computed GCD
        return str1[: gcd(len(str1), len(str2))]