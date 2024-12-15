const translateMap = {"G": "C", "C": "G", "T": "A", "A": "U"}

export const toRna = (string) => {
  let arr = string.split("")
  let result = []
  for (let item of arr) {
    result.push(translateMap[item])
  }
  console.log(result)
  return result.join("")
};