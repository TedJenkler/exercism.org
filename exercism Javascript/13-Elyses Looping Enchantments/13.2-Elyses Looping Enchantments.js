export function cardTypeCheck(stack, card) {
    let count = 0
    stack.forEach((item) => {
      if (item === card) {
        count++;
      }
    });
    return count
  }
  
  export function determineOddEvenCards(stack, type) {
    let count = 0
    stack.forEach((item) => {
      if (type && item % 2 == 0) {
        count++
      }
      else if(!type && item % 2 != 0) {
        count++
      }
    })
    return count
  }