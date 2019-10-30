"""
This is a typical DFS problem, we increase the number of island every time we found a '1' in the grid. Then we applied
DFS to this grid and transform every '1' to '0'.
"""


class Solution:
    def numIslands(self, grid: list) -> int:
        num_island = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '0':
                    continue
                else:
                    num_island += 1
                    grid[row][col] = '0'
                    dfs_list = [[row, col]]
                    while dfs_list:
                        cur_loc = dfs_list.pop()
                        cur_row = cur_loc[0]
                        cur_col = cur_loc[1]
                        for i in range(-1, 2, 1):
                            for j in range(-1, 2, 1):
                                if i == j or i * j != 0:
                                    continue
                                new_row = cur_row + i
                                new_col = cur_col + j
                                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '1':
                                    dfs_list.append([new_row, new_col])
                                    grid[new_row][new_col] = '0'
        return num_island
