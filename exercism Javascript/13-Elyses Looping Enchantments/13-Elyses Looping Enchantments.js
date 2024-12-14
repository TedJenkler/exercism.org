/**
 * Determine how many cards of a certain type there are in the deck
 *
 * @param {number[]} stack
 * @param {number} card
 *
 * @returns {number} number of cards of a single type there are in the deck
 */
export function cardTypeCheck(stack, card) {
    let total = 0
    stack.forEach((item) => {
      if(item === card) {
        total++
      }
    })
    return total
  }
  
  /**
   * Determine how many cards are odd or even
   *
   * @param {number[]} stack
   * @param {boolean} type the type of value to check for - odd or even
   * @returns {number} number of cards that are either odd or even (depending on `type`)
   */
  export function determineOddEvenCards(stack, type) {
    let total = 0
    for(let num of stack) {
      if(type === true && num % 2 === 0) {
      total++
      }else if (type === false && num % 2 !== 0) {
        total++
      }
    }
    return total
  }