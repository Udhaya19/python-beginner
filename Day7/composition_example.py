class Department:
    def __init__(self, dept_name, student_name):
        self.dept_name = dept_name
        self.student_name = student_name

    def get_student_details(self):
        print("Department :{} && Student name :{}".format(self.dept_name, self.student_name))


class Institution:
    def __init__(self, inst_name, department):
        self.inst_name = inst_name
        self.pp = department

    def get_institution_details(self):
        print("Institution details:", self.inst_name, self.pp.get_student_details())


d = Department("CSE", "udhaya")
i = Institution("Agni", d)
i.get_institution_details()
