"""
Ashley Piccone

Euler Problem #15: Lattice paths
"""

# add up all the routes to get to each position as we make our way diagonally
def routes(dim):
    # 20D array filled with ones
    arr = [1] * dim
    # for i in the 20 spots
    for i in range(dim):
        # for j up until each spot
        for j in range(i):
            # previous choices
            arr[j] = arr[j] + arr[j-1]
        # two directions to go
        arr[i] = 2 * arr[i-1]
    return arr[dim-1]

num = routes(20)
print(num)

