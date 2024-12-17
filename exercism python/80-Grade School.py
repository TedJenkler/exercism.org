class School:
    def __init__(self):
        self.students = {}
        self.called = []

    def add_student(self, name, grade):
        for students_in_grade in self.students.values():
            if name in students_in_grade:
                self.called.append(False)
                return

        if grade not in self.students:
            self.students[grade] = []

        self.students[grade].append(name)
        self.called.append(True)

    def roster(self):
        result = []
        for grade in sorted(self.students.keys()):
            result.extend(sorted(self.students[grade]))
        return result

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, []))

    def added(self):
        return self.called