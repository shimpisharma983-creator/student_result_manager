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


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"


def main():
    n = int(input("Enter number of students: "))

    for i in range(n):
        print("\n--- Student", i + 1, "---")

        name = get_valid_name()
        roll = get_valid_roll()

        physics = get_valid_marks("Physics")
        chemistry = get_valid_marks("Chemistry")
        maths = get_valid_marks("Maths")

        total = physics + chemistry + maths
        percentage = total / 3
        grade = calculate_grade(percentage)

        print("\n--- Result ---")
        print("Name:", name)
        print("Roll:", roll)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)



if __name__ == "__main__":
    main()







