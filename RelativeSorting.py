def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        li_dif=[n for n in arr1 if n not in arr2]
        print(li_dif)
        li_dif.sort()
        res = []
        arr1_cnt = collections.Counter(arr1)
        print(arr1_cnt)
        for n in arr2:
            res =res+ [n] * arr1_cnt[n]
        
    
        res=res+li_dif
        return res
        