n, t = input().split()
n, t = int(n), int(t) - 1

cells = input().split()

actual_cell = 0
cell_value = 0

while(actual_cell < t):
    cell_value = int(cells[actual_cell])
    actual_cell += cell_value

if(actual_cell == t):
    print("YES")
else:
    print("NO")