MAX = 1000
MIN = -1000
def minimax(depth, index, maximizing, values, alpha, beta):

    if depth == 2:
        return values[index]

    if maximizing:
        best = MIN

        for i in range(2):
            value = minimax(depth + 1, index * 2 + i,
                            False, values, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best
    else:
        best = MAX

        for i in range(2):
            value = minimax(depth + 1, index * 2 + i,
                            True, values, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best
# 1 = Goal, 0 = Save
values = [1, 0, 0, 1]
result = minimax(0, 0, True, values, MIN, MAX)
print("Best Shooting Value:", result)
if result == 1:
    print("Best Strategy: Shoot")
else:
    print("Best Strategy: Goalkeeper can save")
