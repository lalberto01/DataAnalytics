# Description: This script works with a list of favorite movies

# 1. Create a list of favorite movies
movies = ["Avatar", "Mean Girls", "The Notebook"]

# 2. Print description using len()
print(f"The list movies includes my top {len(movies)} favorite movies")

# Print full list
print(movies)

# -------------------------
# 3. Print sorted list using sorted()
# -------------------------

print(sorted(movies))   # Temporary sorted version
print(movies)           # Original list stays the same

# Notice:
# sorted() prints a sorted copy, but does not change the original list

# -------------------------
# 4. Use .sort()
# -------------------------

movies.sort()
print(movies)

# Notice:
# .sort() changes the original list permanently

# -------------------------
# 5. Add another movie
# -------------------------

movies.append("Inside Out")

# Updated description
print(f"The list movies includes my top {len(movies)} favorite movies")

# Print updated list
print(movies)