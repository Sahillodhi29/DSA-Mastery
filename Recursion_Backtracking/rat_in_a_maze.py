def is_safe(x, y, maze, visited, n):
    # first conditon to check x in boundary , second to check y in boundary ,
    # third checking is it a valid step like 1 or not , and last condition to
    # check is it should not be visited!
    return  0 <= x < n and 0 <= x < n and maze[x][y] == 1 and not visited[x][y]


# recursive 
def solve_maze(x, y, n, path, maze, visited, paths):
    
    #base case
    if x == n-1 and y == n-1:
        paths.append(path)  # Save the valid path
        return
    
    # Mark current cell as visited
    visited[x][y] = True
    
    directions = [('D', x+1, y),('L', x, y-1),
                  ('R', x, y+1), ('U', x-1, y)]
    
    
    for move, next_x, next_y in directions:
        if is_safe(next_x, next_y, maze, visited, n):
           solve_maze(next_x, next_y, n, path+move, maze, visited, paths) 
           
    visited[x][y] = False


def find_paths(maze, n):
    visited = [[False for _ in range(n)] for _ in range(n)]
    paths = []
    
    if maze[0][0] == 1:
        solve_maze(0, 0, n, "" , maze, visited, paths)
        
    return paths


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

n = len(maze)
all_paths = find_paths(maze, n)

print("All paths from start to end:")
for p in all_paths:
    print(p)
        