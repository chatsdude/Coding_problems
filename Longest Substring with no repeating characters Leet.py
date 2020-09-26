def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        cnt=0
        for r in range(len(s)):
            if s[r] not in d:
                cnt=max(cnt,r-l+1)
            else:
                if d[s[r]]<l:
                    cnt=max(cnt,r-l+1)
                else:
                    l=d[s[r]] + 1
            d[s[r]]=r
        return cnt