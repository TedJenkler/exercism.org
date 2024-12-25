const points = { "1": ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], "2": ["D", "G"], "3": ["B", "C", "M", "P"], "4": ["F", "H", "V", "W", "Y"], "5": ["K"], "8": ["J", "X"], "10": ["Q", "Z"]}

export const score = (word) => {
  let upperWord = word.toUpperCase().split("")
  let total = 0
  for (let letter of upperWord) {
    for (let key in points) {
      if (points[key].includes(letter)) {
        total += Number(key)
      }
    }
  }
  return total
};