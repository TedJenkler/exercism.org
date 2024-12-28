export const countWords = (word) => {
    let count = {}
    let cleaned = word.toLowerCase().split(/[^a-zA-Z0-9']+/)
      .filter(item => item !== "");
    
    for (let item of cleaned) {
      if (item[0] === "'") {
        item = item.slice(1);
      }
      if (item[item.length - 1] === "'") {
        item = item.slice(0, item.length - 1);
      }
      
      if (count.hasOwnProperty(item)) {
        count[item] += 1
      }else {
        count[item] = 1
      }
    }
    return count
  };