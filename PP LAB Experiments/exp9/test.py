
# Test Module
# test.py
from university.result import UniversityResult
from university.college.exam import CollegeExam

def getdata():
    # Accessing data from both University and College packages
    university_result = UniversityResult("John", 75)
    college_exam_data = CollegeExam.get_exam_data()
    return university_result, college_exam_data

def display():
    # Displaying data
    university_result, college_exam_data = getdata()
    print("University Result:")
    print(f"Student Name: {university_result.student_name}")
    print(f"Marks: {university_result.marks}")
    print("\nCollege Exam Data:")
    print(f"Subject: {college_exam_data['subject']}")
    print(f"Exam Date: {college_exam_data['exam_date']}")
    print(f"Marks: {college_exam_data['marks']}")

if __name__ == "__main__":
    display()
