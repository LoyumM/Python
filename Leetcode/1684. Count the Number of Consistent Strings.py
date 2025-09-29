# You are given a string allowed consisting of distinct characters and an array of strings words. 
# A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        return len(words) - count
    

# using dictionary
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        # Create a dictionary from allowed characters
        allowed_dict = {char: True for char in allowed}
        
        count = 0
        
        for word in words:
            is_consistent = True
            for letter in word:
                if letter not in allowed_dict:
                    is_consistent = False
                    break
            if is_consistent:
                count += 1
                
        return count

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
instance = Solution()
print(instance.countConsistentStrings(allowed, words))