export function countNucleotides(strand) {
    let valid = ['A', 'C', 'G', 'T']
    let count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    let arr = strand.split("")
    for (let i = 0; i < arr.length; i++) {
      if (valid.includes(arr[i])) {
        if (count.hasOwnProperty(arr[i])) {
          count[arr[i]] += 1
        }
      }else {
        throw Error("Invalid nucleotide in strand")
      }
    }
    return Object.values(count).join(" ")
  }