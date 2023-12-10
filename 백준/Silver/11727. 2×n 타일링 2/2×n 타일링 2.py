tiles_table = [0] * 1001

def get_tiles(x):
    if x == 1: return 1
    if x == 2: return 3
    if tiles_table[x]: return tiles_table[x]
    tiles_table[x] = (get_tiles(x-1) + 2 * get_tiles(x-2)) % 10007
    return tiles_table[x]

n = int(input())
print(get_tiles(n))