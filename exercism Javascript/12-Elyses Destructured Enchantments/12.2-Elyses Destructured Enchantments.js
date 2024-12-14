export function getFirstCard(deck) {
    const [nr1] = deck
    return nr1
  }
  
  export function getSecondCard(deck) {
    const [nr1, nr2] = deck
    return nr2
  }
  
  export function swapTopTwoCards(deck) {
    const [nr1, nr2, ...rest] = deck
    deck = [nr2, nr1, ...rest]
    return deck
  }
  
  export function discardTopCard(deck) {
    const [nr1, ...rest] = deck
    return [nr1, rest]
  }
  
  const FACE_CARDS = ['jack', 'queen', 'king'];
  
  export function insertFaceCards(deck) {
    const [nr1, ...rest] = deck
    return [nr1, ...FACE_CARDS, ...rest]
  }