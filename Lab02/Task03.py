# CSE325-2026-L02-M4RB-T3

QUALITY_BASELINE = "refactored"


def letter_grade(average):
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def performance_status(average):
    if average >= 90:
        return "Excellent"
    if average >= 80:
        return "Very Good"
    if average >= 70:
        return "Good"
    if average >= 60:
        return "Average"
    if average >= 50:
        return "Pass"
    return "Fail"


def create_result(student):
    total = sum(student["marks"])
    average = total / len(student["marks"])

    return {
        "name": student["name"],
        "average": average,
        "grade": letter_grade(average),
        "status": performance_status(average)
    }


def print_report(results):
    for result in results:
        print("------------------------")
        print("Student:", result["name"])
        print("Average:", result["average"])
        print("Grade:", result["grade"])
        print("Status:", result["status"])


def process_students():
    students = [
        {"name": "Ali", "marks": [80, 75, 90]},
        {"name": "Ahmed", "marks": [65, 70, 60]},
        {"name": "Sara", "marks": [92, 88, 95]},
        {"name": "Hassan", "marks": [55, 62, 58]},
        {"name": "Ayesha", "marks": [45, 50, 48]}
    ]

    results = [create_result(student) for student in students]

    print_report(results)

    return results


def main():
    process_students()


if __name__ == "__main__":
    main()

# Measured against the construction baseline.
# CSE325-2026-L02-M4RB-T3