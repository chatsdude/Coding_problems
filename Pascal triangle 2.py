 '''Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.'''

 def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        if rowIndex==0:
            return [1]
        res.append([1])
        if rowIndex==1:
            return [1,1]
        for i in range(1,rowIndex+1):
            current=[]
            current.append(1)
            for j in range(1,i):
                current.append(res[i-1][j-1] + res[i-1][j])
            current.append(1)
            res.append(current)
        return res[-1]