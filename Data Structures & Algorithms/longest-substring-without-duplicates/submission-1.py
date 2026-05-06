class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length  = 0
        sub_set = list()
        for i in range(len(s)):
            if s[i] in sub_set:
                index = sub_set.index(s[i])
                sub_set = list(sub_set[index+1::])
                print('after Update',sub_set)
                sub_set.append(s[i])
                print('after append',sub_set)

            else:
                sub_set.append(s[i])
            max_length = max(max_length, len(sub_set))
            print(sub_set, max_length)
        return max_length