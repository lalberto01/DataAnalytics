import random
import math
import statistics

# Create starting variables

vals_1_100 = range(1, 100)

vals_sample = random.sample(vals_1_100, 75)

vals_choices = random.choices(vals_1_100, k=200)

radius = random.randint(3, 10)

pi = math.pi

# -------------------------------
# Experimenting with subset (1–100)
# -------------------------------

# Sum of 75 sample values
sample_sum = sum(vals_sample)

# Average of 75 sample values
sample_avg = statistics.mean(vals_sample)

# Median of 75 sample values
sample_median = statistics.median(vals_sample)


# -------------------------------
# Experimenting with superset (200 values with replacement)
# -------------------------------

# Average
choices_avg = statistics.mean(vals_choices)

# Median
choices_median = statistics.median(vals_choices)

# Mode
choices_mode = statistics.mode(vals_choices)

# Standard deviation
choices_stdev = statistics.stdev(vals_choices)

# Variance
choices_var = statistics.variance(vals_choices)


# -------------------------------
# Modeling a random circle
# -------------------------------

# First circle
area_1 = math.pi * radius ** 2
area_1_ceil = math.ceil(area_1)
area_1_floor = math.floor(area_1)

# Second circle (new radius)
radius_2 = random.randint(3, 10)
area_2 = math.pi * radius_2 ** 2
area_2_ceil = math.ceil(area_2)
area_2_floor = math.floor(area_2)


# -------------------------------
# FINAL OUTPUT
# -------------------------------

print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", sample_sum)
print("Average of 75 sample values:", sample_avg)
print("Median of 75 sample values:", sample_median)

print('\n')

print("_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", choices_avg)
print("Median of 200 values:", choices_median)
print("Mode of 200 values:", choices_mode)
print("Standard deviation of 200 values:", choices_stdev)
print("Variance of 200 values:", choices_var)

print('\n')

print("_Modeling a random circle:")
print("Radius =", radius, ", area =", area_1_ceil, "(rounded up)")
print("Radius =", radius, ", area =", area_1_floor, "(rounded down)")