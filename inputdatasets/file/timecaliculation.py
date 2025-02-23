import timeit

# Hard-coded approach
def hard_coded_update(row):
    row[1] = "New Name"
    row[2] = "New Department"
    row[3] = "New Salary"

# Dynamic approach
fields = ["ID", "Name", "Department", "Salary"]

def dynamic_update(row):
    for i, field in enumerate(fields):
        row[i] = f"New {field}"

# Row sample data
row = ["101", "John Doe", "Engineering", "50000"]

# Timing both approaches
print("Hard-Coded Time:", timeit.timeit(lambda: hard_coded_update(row.copy()), number=100000))
print("Dynamic Time:", timeit.timeit(lambda: dynamic_update(row.copy()), number=100000))
