class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = list(s)
        print(string)
        res = []
        for char in string:
            if char.isalnum():
                res.append(char.lower())
            else:
                pass
        result = ''.join(res)
        print(result)
        return (result == result[::-1])