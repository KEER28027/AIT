distance = [
    [0, 10, 12, 11, 14],
    [10, 0, 13, 15, 8],
    [12, 13, 0, 9, 14],
    [11, 15, 9, 0, 16],
    [14, 8, 14, 16, 0]
]

route = [0]
unvisited = [1, 2, 3, 4]

while unvisited:
    current = route[-1]

    next_city = min(
        unvisited,
        key=lambda x: distance[current][x]
    )

    route.append(next_city)
    unvisited.remove(next_city)

route.append(0)

total = 0

for i in range(len(route) - 1):
    total += distance[route[i]][route[i + 1]]

print("Best Route:", [x + 1 for x in route])
print("Minimum Distance:", total)
