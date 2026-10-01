n = int(input("Enter the number of towers: "))

signals = []

print("Enter the signal strength of each tower:")
for i in range(n):
    signal = int(input(f"Tower {i + 1}: "))
    signals.append(signal)

current = int(input("Enter the starting tower position (1 to {}): ".format(n)))
current = current - 1

path = [current + 1]

while True:
    best = current

    # Check left neighbour
    if current > 0 and signals[current - 1] > signals[best]:
        best = current - 1

    # Check right neighbour
    if current < n - 1 and signals[current + 1] > signals[best]:
        best = current + 1

    # Stop if no better neighbour
    if best == current:
        break

    current = best
    path.append(current + 1)

print("\nPath followed:", end=" ")
for tower in path:
    print("Tower", tower, end=" ")

print("\nStrongest Signal:", signals[current])
print("Best Tower:", current + 1)
