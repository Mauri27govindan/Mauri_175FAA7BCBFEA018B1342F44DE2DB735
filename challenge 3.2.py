class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"


def sort_students(students):
    """
    Sorts a list of student objects based on their CGPA in descending order.
    
    Args:
    - students (list): List of student objects.
    
    Returns:
    - list: Sorted list of student objects based on CGPA in descending order.
    """
    return sorted(students, key=lambda x: x.cgpa, reverse=True)


# Testing the sort_students function
if __name__ == "__main__":
    # Create a list of student objects with different CGPAs
    students_list = [
        Student(name="John", roll_number="101", cgpa=3.5),
        Student(name="Doe", roll_number="102", cgpa=3.2),
        Student(name="Alice", roll_number="103", cgpa=3.8),
        Student(name="Bob", roll_number="104", cgpa=3.1),
    ]

    # Display the initial list of students
    print("Initial List of Students:")
    for student in students_list:
        print(student)

    # Sort the list of students based on CGPA in descending order
    sorted_students = sort_students(students_list)

    # Display the sorted list of students
    print("\nSorted List of Students based on CGPA (Descending Order):")
    for student in sorted_students:
        print(student)
