class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        list_s = list(s)
        list_t = list(t)

        for i in list_s:
            if i in list_t:
                list_t.remove(i)
        
        return len(list_t) == 0