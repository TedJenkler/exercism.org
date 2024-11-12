"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    rounded = []
    while student_scores:
        student = student_scores.pop()
        rounded.append(round(student))
    return rounded


def count_failed_students(student_scores):
    count = 0
    for student in student_scores:
        if student <= 40:
            count = count + 1
    return count

def above_threshold(student_scores, threshold):
    passed = []
    for score in student_scores:
        if score >= threshold:
            passed.append(score)
    return passed


def letter_grades(highest):
    interval = (highest - 40) // 4
    thresholds = [41 + interval * i for i in range(4)]
    return thresholds


def student_ranking(student_scores, student_names):
    grades = []
    for index, name in enumerate(student_names):
        grades.append(f"{index + 1}. {name}: {student_scores[index]}")
    return grades


def perfect_score(student_info):
    perfect = []
    for student in student_info:
        if student[1] == 100:
            return student
    return perfect