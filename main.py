def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid name! Use alphabets only.")




def get_valid_roll():
    while True:
        roll = input("Enter your roll number: ")
        if roll.isdigit():
            return roll
        else:
            print("Invalid roll number! Enter numbers only.")




def get_valid_marks(subject):
    while True:
      try:  
        marks = int(input(f"{subject} marks: "))
        if 0 <= marks <= 100:
            return marks
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")
      except ValueError:
            print("Invalid input! Please enter numeric value only.")



n=int(input("Enter the number of students :-"))
for i in range(n):
 print("---- students",i+1,"-----")
 name=get_valid_name()
 roll=get_valid_roll()
 m1=get_valid_marks("Physics")
 m2=get_valid_marks("chemistry")
 m3=get_valid_marks("maths")


 total = m1 + m2 + m3
 percentage = total / 3


 if percentage >= 90:
    grade = "A"
 elif percentage >= 75:
    grade = "B"
 elif percentage >= 60:
    grade = "C"
 else:
    grade = "Fail"


 print("\n--- Result ---")
 print("Name:", name)
 print("Roll:", roll)
 print("Total Marks:", total)
 print("Percentage:", percentage)
 print ("grade:-",grade)







