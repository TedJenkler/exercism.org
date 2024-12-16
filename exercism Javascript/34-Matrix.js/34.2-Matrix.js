export class Matrix {
    constructor(matrix) {
      this.matrix = matrix.split("\n")
    }
  
    get rows() {
      let rows = [];
      for (let row of this.matrix) {
        rows.push(row.split(" ").map(num => Number(num)));
      }
      return rows;
    }
  
    get columns() {
      let rows = this.rows;
      let columns = [];
  
      for (let colIndex = 0; colIndex < rows[0].length; colIndex++) {
        let column = [];
        for (let row of rows) {
          column.push(row[colIndex]);
        }
        columns.push(column);
      }
      
      return columns;
    }
  }