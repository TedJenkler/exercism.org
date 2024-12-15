export function seeingDouble(deck) {
    return deck.map((item) => item * 2)
  }
  
  export function threeOfEachThree(deck) {
    let result = []
    deck.forEach((item) => {
      if (item == 3) {
        result.push(3)
        result.push(3)
        result.push(3)
      }
      else {
        result.push(item)
      }
    })
    return result
  }
  
  export function middleTwo(deck) {
    return [deck[deck.length / 2 - 1], deck[deck.length / 2]]
  }
  
  export function sandwichTrick(deck) {
    deck.splice(deck.length / 2, 0, deck[0])
    deck.splice(deck.length / 2, 0, deck[deck.length - 1])
    deck.pop()
    deck.shift()
    return deck
  }
  
  export function twoIsSpecial(deck) {
    return deck.filter((item) => item == 2)
  }
  
  export function perfectlyOrdered(deck) {
    return deck.sort((a, b) => a - b)
  }
  
  export function reorder(deck) {
    return deck.reverse()
  }