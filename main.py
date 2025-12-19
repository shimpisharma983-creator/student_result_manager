name=input("enter your name:-")
roll=int(input("Enter your roll number:-"))



m1=int(input("physics marks:-"))
m2=int(input("chemistry marks:-"))
m3=int(input("maths marks:-"))


total = m1 + m2 + m3
percentage = total / 3

print("\n--- Result ---")
print("Name:", name)
print("Roll:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)
if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("Result:", result)








