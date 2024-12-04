export function twoSum(array1, array2) {
    return Number(array1.join("")) + Number(array2.join(""))
  }
  
  export function luckyNumber(value) {
    return value === Number(String(value).split("").reverse().join(""))
  }
  
  export function errorMessage(input) {
    if (input === "" || input === null || input === undefined) {
      return 'Required field';
    }
  
    const numberInput = Number(input);
    if (Number.isNaN(numberInput) || numberInput === 0) {
      return 'Must be a number besides 0';
    }
  
    return '';
  }