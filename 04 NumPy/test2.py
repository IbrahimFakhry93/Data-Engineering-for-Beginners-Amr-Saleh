import numpy as np

tree_census = np.array(
    [
        [1001, 501, 12, 30],
        [1002, 502, 15, 45],
        [1003, 501, 10, 25],
        [1004, 503, 20, 50],
        [1005, 502, 18, 40],
    ]
)

# Select all rows of block ID data from the second column
block_ids = tree_census[:, 1]

print(block_ids)
