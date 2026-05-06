class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0  # Left and right pointers
        max_length = 0
        substring = set()  # Use a set for faster lookups and to store unique characters
        
        while r < len(s):
            if s[r] not in substring:  # If character at r is not in the current substring
                substring.add(s[r])    # Add it to the substring
                max_length = max(max_length, r - l + 1)  # Update max_length
                r += 1
            else:
                substring.remove(s[l])  # Remove character at l from the substring
                l += 1  # Move the left pointer right to shrink the window
        
        return max_length
