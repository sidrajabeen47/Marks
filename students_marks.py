# 1.list of student marks
marks = [55, 42, 78, 35, 90]
pass_mark = 40

# 2.new list with True (pass) or False (fail) for each subject

results = [score >= pass_mark for score in marks]

print(f"Marks: {marks}")
print(f"Pass/Fail List: {results}")

# if all subjects passed
all_passed = all(results) 

#If the student passed at least one subject (using any() as requested)
at_least_one_pass = any(results)

print(f"Passed all subjects? {all_passed}")
print(f"Passed at least one subject? {at_least_one_pass}")
