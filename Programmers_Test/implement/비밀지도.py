def solution(n, arr1, arr2):
    answer = []
    first_maze = []
    second_maze = []

    make_maze(n, arr1, first_maze)
    make_maze(n, arr2, second_maze)

    for i in range(n):
        result = ""
        for j in range(n):
            if first_maze[i][j] == second_maze[i][j] and first_maze[i][j] == " ":
                result += " "
            else:
                result += "#"
        answer.append(result)
    return answer


def make_maze(size, maze, result):
    for i in maze:
        wall = ""
        number = i
        for j in range(size-1, -1, -1):
            if number >= 2**j:
                number -= 2**j
                wall += "#"
            else:
                wall += " "
        result.append(wall)
