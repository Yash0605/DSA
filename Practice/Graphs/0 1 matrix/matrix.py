from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        BFS solution
        --------------------
        In this case we need to start from source and get the min distance for the destination
        We know 1 is the destination so 0 will be our source.
        We will traverse the matrix and push in all the cells wich are 0 for source
        At the same time we will mark all the cells with 1 with the max possible cell value 
            => i.e m+n considering the case of only one 0 in matrix which is at n-1, m-1 so cell 0,0 has nearest 0 at n+m
        This way we do need to maintain a visited matrix as while traversal if the new neighbor val is < than current neighbor val we will update the cell val
            irrespective of whether it has been visited or not
        '''
        n,m = len(mat), len(mat[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = m+n

        # Since there will be atleast one 0 the queue will always have a starting value
        # for each cell we need to check in 4 directions for neighbors and update their val if >0
        delta_directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while len(q)>0:
            i,j = q.popleft()

            for k in range(4):
                new_i = i+delta_directions[k][0]
                new_j = j+delta_directions[k][1]

                # if the neighbor val > 0 and cell val = 0 then we check if 0+1 < neighbor val => replace if this is the case
                if new_i>=0 and new_i<n and new_j>=0 and new_j<m and mat[new_i][new_j] > mat[i][j]+1:
                    mat[new_i][new_j] = mat[i][j]+1
                    q.append((new_i,new_j))

        return mat



