def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        res = 1

        for index in range(len(s)):
            sub_s = ''
            sub_s += s[index]
            if s[min(index+1, len(s)-1)] in sub_s:
                continue
            for subsq_index in range(index + 1,len(s)):
                if s[subsq_index] in sub_s:
                    res = max(res,len(sub_s))
                    break
                               
                sub_s += s[subsq_index]
                
                if subsq_index == len(s) -1:
                    res = max(res,len(sub_s))
        return res
print(lengthOfLongestSubstring("au"))