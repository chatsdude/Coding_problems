'''In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=[]
        safe=[]
        row,col=len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    rotten.append((i,j))
                if grid[i][j]==1:
                    safe.append((i,j))
        if not grid or (len(safe)>0 and len(rotten)==0) :
            return -1
        if len(safe)==0:
            return 0
        min_count=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        while len(safe) > 0:
            infected=[]
            for rot in rotten:
                rot_coord1=rot[0]
                rot_coord2=rot[1]
                for x,y in directions:
                    new_coord1=rot_coord1 + x
                    new_coord2=rot_coord2 + y
                    if (new_coord1,new_coord2) in safe:
                        infect=safe.pop(safe.index((new_coord1,new_coord2)))
                        infected.append(infect)
            if len(infected)==0:
                return -1
            rotten=infected
            min_count+=1
        return min_count
