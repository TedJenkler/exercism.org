export const decodedValue = (arr) => {
    let total = "";
    for (let bands of arr) {
      if (total.length < 2) {
        switch (bands) {
          case 'black':
            total += "0";
            break;
          case 'brown':
            total += "1";
            break;
          case 'red':
            total += "2";
            break;
          case 'orange':
            total += "3";
            break;
          case 'yellow':
            total += "4";
            break;
          case 'green':
            total += "5";
            break;
          case 'blue':
            total += "6";
            break;
          case 'violet':
            total += "7";
            break;
          case 'grey':
            total += "8";
            break;
          case 'white':
            total += "9";
            break;
        }
      }
    }
    return Number(total);
  };
  