export class Triangle {
    constructor(...sides) {
      this.tri = [...sides]
      const [a, b, c] = this.tri
      this.a = a
      this.b = b
      this.c = c
    }
  
    isTri() {
      if (this.a + this.b >= this.c && this.b + this.c >= this.a && this.a + this.c >= this.b && this.a > 0 && this.b > 0 && this.c > 0) {
        return true
      }else {
        return false
      }
    }
  
    get isEquilateral() {
      if (this.isTri() && this.a == this.b && this.b == this.c) {
        return true
      }else {
        return false
      }
    }
  
    get isIsosceles() {
      if (this.isTri() && new Set(this.tri).size < 3) {
        return true
      }else {
        return false
      }
    }
  
    get isScalene() {
      if (this.isTri() && new Set(this.tri).size == 3) {
        return true
      }else {
        return false
      }
    }
  }