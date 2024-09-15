export const isPangram = (sentence) => {
    let arr = sentence.toLowerCase().split("");
    let set = new Set();
    
    for (let i = 0; i < arr.length; i++) {
      if (arr[i].match(/^[a-zA-Z]$/)) {
        set.add(arr[i]);
      }
    }
    
    if (set.size === 26) {
      return true;
    } else {
      return false;
    }
  };