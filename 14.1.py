class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender},{self.age},{self.first_name},{self.last_name}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        Human.__init__(self, gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{Human.__str__(self)}, {self.record_book}'

class GroupFullException(Exception):
    pass

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException()
        if student not in self.group:
            self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student in self.group:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Group number: {self.number}\n{all_students.strip()}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN101')
st4 = Student('Female', 24, 'Anna', 'Smith', 'AN102')
st5 = Student('Male', 21, 'Mike', 'Johnson', 'AN103')
st6 = Student('Female', 23, 'Emily', 'Taylor', 'AN104')
st7 = Student('Male', 25, 'David', 'Brown', 'AN105')
st8 = Student('Female', 22, 'Sophia', 'Anderson', 'AN106')
st9 = Student('Male', 26, 'Chris', 'Wilson', 'AN107')
st10 = Student('Female', 20, 'Laura', 'White', 'AN108')
st11= Student('Male', 23, 'Brian', 'Martin', 'AN109')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
try:
    gr.add_student(st11)
except GroupFullException as e:
    print('ERROR: Group is full!')
