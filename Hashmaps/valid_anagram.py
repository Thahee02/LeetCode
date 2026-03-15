class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
    

# Example usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True