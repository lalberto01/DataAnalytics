# tiles.py
# Calculate how many boxes of tiles are needed

import math

# Example room dimensions (feet)
length = 10
width = 12

# Calculate room area
total_tiles_needed = length * width

# Each box has 12 tiles
boxes_needed = math.ceil(total_tiles_needed / 12)

# Add 10% extra tiles
tiles_with_extra = total_tiles_needed * 1.10

# Full boxes only
total_boxes_to_buy = math.ceil(tiles_with_extra / 12)

# Results
print(f"Room size: {length} ft x {width} ft")
print(f"Tiles needed: {total_tiles_needed}")
print(f"Boxes needed: {boxes_needed}")
print(f"Boxes to buy with 10% extra: {total_boxes_to_buy}")