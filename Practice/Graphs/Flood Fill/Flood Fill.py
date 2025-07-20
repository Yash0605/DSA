class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        need to update all the linked same color pixels with the given color
        """
        m = len(image)
        n = len(image[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        originalColor = image[sr][sc]

        if originalColor == color:
            return image

        def dfs(sr, sc):
            for dx, dy in directions:
                x = sr + dx
                y = sc + dy

                if 0 <= x < m and 0 <= y < n and image[x][y] == originalColor:
                    image[x][y] = color
                    dfs(x, y)

        image[sr][sc] = color
        dfs(sr, sc)

        return image
