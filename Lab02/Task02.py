# Student data is kept separate from processing logic
# Principle: Separation of Data and Logic
students = [
    {"name": "Salman", "marks": [80, 75, 90]},
    {"name": "Ahmed", "marks": [65, 70, 60]},
    {"name": "Sara", "marks": [92, 88, 95]},
    {"name": "Hassan", "marks": [55, 62, 58]},
    {"name": "Ayesha", "marks": [45, 50, 48]}
]


# Calculates the average of a student's marks
# Principle: Single Responsibility Principle (SRP)
def calculate_average(marks):
    return sum(marks) / len(marks)


# Determines both grade and status in one place
# Principle: DRY (Don't Repeat Yourself)
# The same average conditions are not repeated in multiple places
def evaluate_performance(average):
    if average >= 90:
        return "A+", "Excellent"
    elif average >= 80:
        return "A", "Very Good"
    elif average >= 70:
        return "B", "Good"
    elif average >= 60:
        return "C", "Average"
    elif average >= 50:
        return "D", "Pass"
    else:
        return "F", "Fail"


# Processes one student at a time
# Principle: Single Responsibility Principle
def process_student(student):
    average = calculate_average(student["marks"])
    grade, status = evaluate_performance(average)

    return {
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    }


# Processes all students
# Principle: Modularity
def process_students(students):
    results = []

    for student in students:
        result = process_student(student)
        results.append(result)

    return results


# Displays the results separately from processing
# Principle: Separation of Concerns
def display_results(results):
    for result in results:
        print("------------------------")
        print("Student:", result["name"])
        print("Average:", result["average"])
        print("Grade:", result["grade"])
        print("Status:", result["status"])


# Main function controls the overall program flow
# Principle: Modular Composition
def main():
    results = process_students(students)
    display_results(results)


# Program starts from main()
if __name__ == "__main__":
    main()