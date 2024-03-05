class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        Merges two strings alternately.
        :type word1: str
        :type word2: str
        :rtype: str
        """

        # Initialize an empty list to store the merged result
        result = []

        # Initialize a counter variable
        i = 0
        
        # Continue iterating until we reach the end of either word1 or word2
        while i < len(word1) or i < len(word2):
            # If there are still characters in word1, append the i-th character to the result
            if i < len(word1):
                result.append(word1[i])
            
            # If there are still characters in word2, append the i-th character to the result
            if i < len(word2):
                result.append(word2[i])

            # Move to the next character
            i += 1

        # Join the characters in the result list to form the final merged string
        return "".join(result)