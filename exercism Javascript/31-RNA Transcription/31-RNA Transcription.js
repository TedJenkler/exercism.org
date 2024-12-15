export const toRna = (dna) => {
    let arr = dna.split("");
    for (let i = 0; i < arr.length; i++) {
      switch (arr[i]) {
        case 'G':
          arr[i] = 'C';
          break;
        case 'C':
          arr[i] = 'G';
          break;
        case 'T':
          arr[i] = 'A';
          break;
        case 'A':
          arr[i] = 'U';
          break;
      }
    }
    return arr.join("");
  };