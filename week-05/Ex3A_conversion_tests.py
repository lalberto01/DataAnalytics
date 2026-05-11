# Description: This script tests various numeric

# -------------------------
# Part 1: Numeric Conversions
# -------------------------

# Original variables
a = " 101.1 "
b = "55"
c = "402 Stevens"
d = "Number 5 "

# a) Cast as integer using int()

# a_int = int(a)       # ValueError (contains decimal and spaces)
b_int = int(b)         # Works
# c_int = int(c)       # ValueError (contains letters)
# d_int = int(d)       # ValueError (contains letters)

# b) Cast as float using float()

a_float = float(a)     # Works
b_float = float(b)     # Works
# c_float = float(c)   # ValueError (contains letters)
# d_float = float(d)   # ValueError (contains letters)

# c) Cast a into float then integer

a_float_int = int(float(a))   # Works = 101

# d) Use slicing to get numeric portion

c_num = int(c[0:3])      # Gets 402
d_num = d[-2]            # Gets "5"

# e) Use .strip() to remove spaces

print(a.strip())         # Removes spaces
print(d.strip())         # Removes spaces

# Print values and types

print(a_float, type(a_float))
print(a_float_int, type(a_float_int))
print(b_int, type(b_int))
print(b_float, type(b_float))
print(c_num, type(c_num))
print(d_num, type(d_num))


# -------------------------
# Lab 2
# File: Ex3A_string_cleaning.py
# -------------------------

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# 3. Convert names to lowercase

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# 4. Convert names to title case

print(name_1.title())
print(name_2.title())
print(name_3.title())

# 5. Remove $ from salary strings

print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))

# Check type (still strings)

print(type(salary_1.replace("$", "")))
print(type(salary_2.replace("$", "")))

# Need int() after removing commas and $

# 6. Chain replace() and int()

clean_salary = int(salary_1.replace("$", "").replace(",", ""))

print(clean_salary)
print(type(clean_salary))