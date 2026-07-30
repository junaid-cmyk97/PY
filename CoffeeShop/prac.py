# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers) # Output: [0, 2, 4, 6, 8]

#pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
#print(pairs) # Output: [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

student = {"name": "Alice", "age": 21, "grade": "A"}

# Using .items()
for key, value in student.items():
    print(f"{key} → {value}")
