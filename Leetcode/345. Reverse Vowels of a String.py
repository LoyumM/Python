class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the string to a list of characters for easy manipulation
        s_list = list(s)
        # Define a set of vowels, both lowercase and uppercase
        vowels = set('aeiouAEIOU')
        
        # Initialize two pointers, one at the start and one at the end of the string
        left, right = 0, len(s_list) - 1
        
        # Continue until the two pointers meet or cross each other
        while left < right:
            # Move the left pointer until it points to a vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move the right pointer until it points to a vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # Swap the vowels pointed to by the left and right pointers
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            # Move the pointers towards each other
            left += 1
            right -= 1
        
        # Convert the list of characters back to a string and return
        return ''.join(s_list)
