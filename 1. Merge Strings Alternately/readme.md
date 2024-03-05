# Merge String alternatively
[Click here to access the problem](https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75)

#####

We first of all start by initializing an empty list to store the merged result

```python
result = []
```

We initialize a counter variable and iterate until the end of either word1 or word2

If there are still characters in word1, we append the i-th character to the result and same for word2

```python
while i < len(word1) or i < len(word2):
    if i < len(word1):
        result.append(word1[i])
    
    if i < len(word2):
        result.append(word2[i])
    i += 1
```

We finish by joining the characters in the result list to form the final merged string

```python
    return "".join(result)
```