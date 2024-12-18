class Garden:
    PLANT_NAMES = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, diagram, students=None):
        if students is None:
            students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

        self.students = sorted(students)
        self.rows = diagram.split("\n")

    def plants(self, student):
        index = self.students.index(student)

        start = index * 2
        end = start + 2

        plant_codes = self.rows[0][start:end] + self.rows[1][start:end]

        return [self.PLANT_NAMES[code] for code in plant_codes]