/**
 * Double every card in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with every card doubled
 */
export function seeingDouble(deck) {
    let arr = deck.map((item) => {
      return item *= 2  
    })
  
    return arr
  }
  
  /**
   *  Creates triplicates of every 3 found in the deck.
   *
   * @param {number[]} deck
   *
   * @returns {number[]} deck with triplicate 3s
   */
  export function threeOfEachThree(deck) {
    let arr = []
  
    deck.forEach((item) => {
      if(item === 3) {
        arr.push(3, 3, 3)
      }else {
        arr.push(item)
      }
    })
    return arr
  }
  
  /**
   * Extracts the middle two cards from a deck.
   * Assumes a deck is always 10 cards.
   *
   * @param {number[]} deck of 10 cards
   *
   * @returns {number[]} deck with only two middle cards
   */
  export function middleTwo(deck) {
    let length = deck.length
    for(let i = 0; i < length - 2; i++) {
      if(i % 2 === 0) {
        deck.pop()  
      }else {
        deck.shift()
      }
    }
    return deck
  }
  
  /**
   * Moves the outside two cards to the middle.
   *
   * @param {number[]} deck with even number of cards
   *
   * @returns {number[]} transformed deck
   */
  
  export function sandwichTrick(deck) {
    const v1 = deck.shift();
    const v2 = deck.pop();
    
    const middleIndex = deck.length / 2;
    
    deck.splice(middleIndex, 0, v2);
    
    deck.splice(middleIndex + 1, 0, v1);
    
    return deck;
  }
  
  /**
   * Removes every card from the deck except 2s.
   *
   * @param {number[]} deck
   *
   * @returns {number[]} deck with only 2s
   */
  export function twoIsSpecial(deck) {
    let arr = deck.filter((item) => item === 2)
    return arr
  }
  
  /**
   * Returns a perfectly order deck from lowest to highest.
   *
   * @param {number[]} deck shuffled deck
   *
   * @returns {number[]} ordered deck
   */
  export function perfectlyOrdered(deck) {
    return deck.sort((a, b) => {
      return a - b
    })
  }
  
  /**
   * Reorders the deck so that the top card ends up at the bottom.
   *
   * @param {number[]} deck
   *
   * @returns {number[]} reordered deck
   */
  export function reorder(deck) {
    return deck.reverse()
  }