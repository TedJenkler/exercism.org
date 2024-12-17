export const rows = (rows) => {
    let pascal = [];
    if (rows === 0) return pascal;
  
    pascal.push([1]);
  
    for (let i = 1; i < rows; i++) {
      let last = pascal[i - 1];
      let newRow = [1];
  
      for (let j = 0; j < last.length - 1; j++) {
        let sum = last[j] + last[j + 1];
        newRow.push(sum);
      }
  
      newRow.push(1);
      pascal.push(newRow);
    }
  
    return pascal;
  };