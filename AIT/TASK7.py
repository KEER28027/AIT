def move(x1, x2):
    return f"Move Monkey from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x):
    return f"Climb box at {x} Up"

def have_banana(x):
    return f"Have banana at {x}"

monkey = int(input("Enter monkey location:"))
banana = int(input("Enter banana location:"))
box = int(input("Enter box location:"))

actions = []

if monkey != box:
    actions.append(move(monkey, box))
    monkey = box

if box != banana:
    actions.append(push_box(box, banana))
    box = banana
    monkey = banana

actions.append(climb_box(banana))
actions.append(have_banana(banana))

print("\nPlan")
for action in actions:
    print(action)
