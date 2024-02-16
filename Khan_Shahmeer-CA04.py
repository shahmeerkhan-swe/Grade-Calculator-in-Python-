#Khan_Shahmeer Nov 2022 CA-04.py

submissions = input("Are there assignments to mark?: (Y/N): ")

while submissions == 'y' or submissions == 'Y':

    student_id = input("\nPlease enter your student ID: ")
    elements = int(input("Please enter the number of elements submitted (1,2, or 3): "))

    if elements > 3 or elements < 1:
        if elements < 1:
            print("No submissions, module failed")
            break
        else:
            print("Not a valid option")
            break

    for x in range(elements):
        print("\nElement",x+1)
        element_grade = int(input("Please enter the grade of this element (50-100): "))
        days_late = int(input("Please enter the number of days late (0,1,2,3,4, or 5): "))

        if element_grade < 50 or elements > 100:
            print("Not a valid grade")
            break

        if days_late == 0:
            final_grade = element_grade - 0
            print("Final grade for this element is:",final_grade)

        elif days_late == 1:
            final_grade = element_grade - 5
            print("Final grade for this element is:",final_grade)

        elif days_late == 2:
            final_grade = element_grade - 10
            print("Final grade for this element is:",final_grade)

        else:
            final_grade = 0
            print("Final grade for this element is:",final_grade)

    submissions = input("\nAre there more assignments to mark?: (Y/N): ")
    
else:
    print("Ending Program...")
