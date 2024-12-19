export class GradeSchool {
    constructor() {
      this.grades = {}  
    }
    
    roster() {
      const sortedGrades = Object.entries(this.grades)
        .sort((a, b) => a[0] - b[0])
        .map(([grade, students]) => [
          grade,
          [...students].sort((a, b) => a.localeCompare(b))
        ]);
  
      return Object.fromEntries(sortedGrades);
    }
  
    add(name, grade) {
      for (let currentGrade in this.grades) {
        if (this.grades[currentGrade].includes(name)) {
          this.grades[currentGrade] = this.grades[currentGrade].filter((value) => value != name)
        }
      }
  
      if (!this.grades.hasOwnProperty(grade)) {
        this.grades[grade] = []
      }
  
      this.grades[grade].push(name)
    }
  
    grade(grade) {
      if (this.grades[grade]) {
        let gradeList = this.grades[grade].sort((a, b) => a.localeCompare(b)); 
         return [...gradeList]
      }else {
        return []
      }
    }
  }