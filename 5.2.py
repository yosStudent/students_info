class Person():
    def __init__(self, first_name, last_name, birth_date, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.id_number = id_number
    
    def show_person_data(self):
        print(f'First Name: {self.first_name}, Last Name: {self.last_name}, Birth Date: {self.birth_date}, ID Number: {self.id_number}')

class Student(Person):
    def __init__(self, first_name, last_name, birth_date, id_number, start_year, end_year, active, major, year_of_study):
        super().__init__(first_name, last_name, birth_date, id_number)
        self.start_year = start_year
        self.end_year = end_year
        self.active = active
        self.major = major
        self.year_of_study = year_of_study
        self.grade_list = GradeList()  # Aggregation relationship

    def print_student_data(self):
        super().show_person_data()
        print(f'Start Year: {self.start_year}, End Year: {self.end_year}, Active: {self.active}, Major: {self.major}, Year of Study: {self.year_of_study}')

class GradeList(dict): 
    def add_subject_and_grade(self, subject, grade):
        self[subject] = grade

    def remove_subject_and_grade(self, subject):
        if subject in self:
            del self[subject]

    def search_subject(self, subject):
        return self.get(subject, "Subject not found")

    def display_subject_table(self):
        print("Subject and Grade Table:")
        for subject, grade in self.items():
            print(f'Subject: {subject}, Grade: {grade}')

class StudentList(dict):
    def add_student(self, index_number, student):
        self[index_number] = student

    def remove_student(self, index_number):
        if index_number in self:
            del self[index_number]

    def find_student(self, index_number):
        return self.get(index_number, "Student not found")

    def display_student_list(self):
        print("Student List:")
        for index_number, student in self.items():
            print(f'Index Number: {index_number}, First Name: {student.first_name}, Last Name: {student.last_name}')

    def display_student_grades(self, index_number):
        student = self.find_student(index_number)
        if student != "Student not found":
            print(f'Grades of student with index number {index_number}:')
            student.grade_list.display_subject_table()

person1 = Person(first_name='Karol', last_name='Kafka', birth_date='12.05.2004', id_number='Not provided')
person2 = Person(first_name='sg', last_name='sg', birth_date='12.05.200sg4', id_number='Not provided')
student1 = Student(first_name='John', last_name='Doe', birth_date='01.01.2000', id_number='ID123456', start_year='2023', end_year='2027', active=True, major='Economics', year_of_study='2')
student2 = Student(first_name='Anna', last_name='Nowak', birth_date='15.09.1985', id_number='ID789012', start_year='2022', end_year='2026', active=True, major='Computer Science', year_of_study='3')

student_list = StudentList()
student_list.add_student('12345', student1)
student_list.add_student('67890', student2)

student1.grade_list.add_subject_and_grade('Mathematics', '5.0')
student1.grade_list.add_subject_and_grade('Physics', '4.5')

student2.grade_list.add_subject_and_grade('Computer Science', '4.0')
student2.grade_list.add_subject_and_grade('Databases', '5.0')

person1.show_person_data()
person2.show_person_data()
student1.print_student_data()
student2.print_student_data()

student_list.display_student_list()
student_list.display_student_grades('12345')
