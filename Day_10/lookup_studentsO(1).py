import time
import sys
def lookup_students(database, student_id):
  for student in database:
    if student["id"] == student_id:
      print(f"Found: {student['name']}(ID: {student_id})")
      return
  print(f"Student with ID {student_id} not found")

#Example databases
small_db = [
  {"id": 101, "name": "Alice"},
  {"id": 102, "name": "Bob"},
  {"id": 103, "name": "Charlie"},
  {"id": 104, "name": "David"},
]

large_db = [
  {"id": i, "name": f"Student{i}"}
  for i in range(1, 10001)
]

print("--- O(n) Time and Space complexity Example---")

#Timing with small database
start1 = time.perf_counter()
lookup_students(small_db, 103)
end1 = time.perf_counter()
print(f"Time taken (small_db): {(end1 - start1) * 1_00_00:.2f} microseconds")

#Timing with large database
start2 = time.perf_counter()
lookup_students(large_db, 9999)
end2 = time.perf_counter()
print(f"Time taken (large_db): {(end2 - start2) * 1_00_00:.2f} microseconds")

#Space complexity demonstration
print("\n--- Space complexity ---")
print(f"Memory used by small_db: {sys.getsizeof(small_db)} bytes")
print(f"Memory used by large_db: {sys.getsizeof(large_db)} bytes")