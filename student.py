"""class for student objects"""
import requests

class Student:
    def __init__(self, firstname, lastname, university, cnp):
        if type(cnp) != int:
            raise ValueError('cpn must be an integer')
        if len(str(cnp)) != 13:
            raise ValueError('CNP must have 13 digits')
        self.firstname = firstname
        self.lastname = lastname
        self.university = university
        self.cnp = cnp
        # self.email = f'{self.firstname.lower()}.{self.lastname.lower()}@{self.university.lower()}.com'
        # self.info_path = f'{self.lastname.lower()}_{self.cnp}.txt'

    @property
    def email(self):
        return f'{self.firstname.lower()}.{self.lastname.lower()}@{self.university.lower()}.com'

    @property
    def info_path(self):
        return f'{self.lastname.lower()}_{self.cnp}.txt'

    def save_student_info(self):
        info = f'{self.firstname}\n' \
               f'{self.lastname}\n' \
               f'{self.university}\n' \
               f'{self.email}\n' \
               f'{self.get_student_classes()}'
        with open(self.info_path, 'w') as f:
            f.write(info)

    def get_student_classes(self):
        response = requests.get('http://127.0.0.1:8000/api/students/1234')
        if response.ok:
            data = response.json()[str(self.cnp)]['Classes']
        else:
            data = 'no data'

        return data


if __name__ == '__main__':
    s1 = Student('Marius', 'Ciurea', 'upb', 1910709282211)
    print(s1.email)
    s1.save_student_info()
    s2 = Student('Dan', 'Chivu', 'upb', 1890709282211)
    print(s2.email)
    s2.save_student_info()
    print(s1.get_student_classes())