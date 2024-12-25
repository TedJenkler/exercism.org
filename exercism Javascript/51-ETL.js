export const transform = (test) => {
  
    let count = {}
    
    for (let item in test) {
      let arr = test[item]
      for (let value of arr) {
          count[value.toLowerCase()] = Number(item)
      }
    }
    return count
  };