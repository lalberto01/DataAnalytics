f = open("about_me.txt", "r")

print(f.read())

f.close()

f = open("about_me.txt", "r")

print(f.read(50))

print()

print(f.read(50))

f.close()

# Readline 

f = open("about_me.txt", "r")

first_chars = f.read(50)

next_lines = []

for i in range(1, 5):
    next_lines.append(f.readline())

next_100 = f.readlines(100)

print("First 50 characters:")
print(first_chars)

print()

print("Next four lines, as list by line:")
print(next_lines)

print()

print("Next 100 characters, as list by line, rounded up to complete lines:")
print(next_100)

f.close()