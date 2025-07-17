class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        same logic as closed islands => remove flood fill and then update the remaining
        '''
        m,n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        def dfs(i,j):
            if visited[i][j]:
                return

            visited[i][j] = True

            for x,y in directions:
                dx = i+x
                dy = y+j

                if 0<=dx<m and 0<=dy<n and board[dx][dy] == 'O':
                    dfs(dx, dy)

        # remove flood fill i.e mark visited
        
        # can be improved - making same mistakes as # of same consecutive diff that I am traversing extra cells which is not required
        # currently m*n but we can do 4 direction seperately so either m or n time
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or i == m-1 or j == 0 or j == n-1:
        #             if board[i][j] == 'O':
        #                 dfs(i,j)

        # top most
        for i in range(0,n):
            if board[0][i] == 'O':
                dfs(0,i)

        # right most
        for i in range(0,m):
            if board[i][n-1] == 'O':
                dfs(i,n-1)

        # bottom most
        for i in range(0,n):
            if board[m-1][i] == 'O':
                dfs(m-1,i)

        # left most
        for i in range(0,m):
            if board[i][0] == 'O':
                dfs(i,0)

        # update the remaining cells
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == 'O':
                    visited[i][j] = True
                    board[i][j] = 'X'

# Time complexity: O(m*n)
# Space complexity: O(m*n) for visited array => can be improved to O(1) by using the board itself