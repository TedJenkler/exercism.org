const allergies = { "eggs": 1, "peanuts": 2, "shellfish": 4, "strawberries": 8, "tomatoes": 16, "chocolate": 32, "pollen": 64, "cats": 128 }

export class Allergies {
  constructor(number) {
    this.number = number
  }

  list() {
    let result = []
    for (let allergy in allergies) {
      if (this.number & allergies[allergy]) {
        result.push(allergy)
      }
    }
    return result
  }

  allergicTo(allergy) {
    if (this.number & allergies[allergy]) {
      return true
    }else {
      return false
    }
  }
}