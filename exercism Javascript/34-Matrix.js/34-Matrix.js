export class Matrix {
    constructor(matrixString) {
      this._rows = matrixString.split("\n").map(row => 
        row.split(" ").map(Number)
      );
    }
  
    get rows() {
      return this._rows;
    }
  
    get columns() {
      const columns = [];
      for (let i = 0; i < this._rows[0].length; i++) {
        columns.push(this._rows.map(row => row[i]));
      }
      return columns;
    }
  }