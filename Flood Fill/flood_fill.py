def flood_fill(image: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
    visited = [[False for _ in range(len(image[0]))]
               for _ in range(len(image))]
    return recursive_fill(image, visited, image[sr][sc], new_color, sr, sc)


def recursive_fill(image: list[list[int]],
                   visited: list[list[bool]],
                   original_color: int,
                   new_color: int,
                   sr: int,
                   sc: int
                   ):
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
        return
    if not visited[sr][sc] and image[sr][sc] == original_color:
        image[sr][sc] = new_color
        visited[sr][sc] = True
        recursive_fill(image, visited, original_color, new_color, sr + 1, sc)
        recursive_fill(image, visited, original_color, new_color, sr - 1, sc)
        recursive_fill(image, visited, original_color, new_color, sr, sc + 1)
        recursive_fill(image, visited, original_color, new_color, sr, sc - 1)
    return image


def print_image(image: list[list[int]]):
    for row in image:
        print(row)


image = [
    [0, 0, 0],
    [0, 0, 0],
]

flood_fill(image, 1, 1, 2)
print_image(image)
