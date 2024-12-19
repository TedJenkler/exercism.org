export const isIsogram = (word) => {
    if (word.trim() == "") return true
    let letters = word.toLowerCase().split("").filter((item) => /[a-z]/.test(item))
    let unique = new Set(letters)
    if (letters.length == unique.size) {
      return true
    }else {
      return false
    }
  };