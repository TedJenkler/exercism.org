const usedNames = new Set()

export class Robot {
  constructor() {
    this._name = this.generateName();
  }

  get name() {
    return this._name;
  }

  generateName() {
    let newName;
    do {
      let letter1 = String.fromCharCode(Math.floor(Math.random() * (90 - 65 + 1)) + 65);
      let letter2 = String.fromCharCode(Math.floor(Math.random() * (90 - 65 + 1)) + 65);
      let num1 = Math.floor(Math.random() * 10);
      let num2 = Math.floor(Math.random() * 10);
      let num3 = Math.floor(Math.random() * 10);
      newName = `${letter1}${letter2}${num1}${num2}${num3}`;
    } while (usedNames.has(newName));

      usedNames.add(newName);
      return newName;
    }
  
  reset() {
    this._name = this.generateName();
  }
}

Robot.releaseNames = () => {
  usedNames.clear();
};