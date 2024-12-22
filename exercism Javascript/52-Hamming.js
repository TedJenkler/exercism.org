export const compute = (strand1, strand2) => {
    let arr1 = strand1.split("")
    let arr2 = strand2.split("")
    if (arr1.length != arr2.length) {
      throw Error("strands must be of equal length")
    }
    let count = 0
    for (let i = 0; i < arr1.length; i++) {
      if (arr1[i] != arr2[i]) {
        count++
      }
    }
    return count
  };