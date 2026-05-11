# Description: This script cleans names and salary data
# Original records
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# -------------------------
# 3. Convert names to lowercase
# -------------------------

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# -------------------------
# 4. Convert names to title case
# -------------------------

print(name_1.title())
print(name_2.title())
print(name_3.title())

# -------------------------
# 5. Remove $ from salaries
# -------------------------

print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))

# Check data types (still strings)
print(type(salary_1.replace("$", "")))
print(type(salary_2.replace("$", "")))

# To perform math next:
# Need to remove commas and convert to int()

# -------------------------
# 6. Chain replace() and int()
# -------------------------

clean_salary = int(salary_1.replace("$", "").replace(",", ""))

print(clean_salary)
print(type(clean_salary))