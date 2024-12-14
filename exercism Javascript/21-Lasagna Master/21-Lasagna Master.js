export function cookingStatus(time) {
    if (time === 0) {
      return 'Lasagna is done.';
    } else if (!isNaN(time)) {
      return 'Not done, please wait.';
    } else {
      return 'You forgot to set the timer.';
    }
  }
  
  export function preparationTime(layers, time) {
    let total = 0;
    if (typeof time === 'number') {
      for (let layer of layers) {
        total += time;
      }
    } else {
      for (let layer of layers) {
        total += 2;
      }
    }
    return total;
  }
  
  export function quantities(layers) {
    let sauce = 0
    let noodles = 0
    for(let layer of layers) {
      if(layer === 'sauce') {
        sauce += 0.2
      }else if(layer === 'noodles') {
        noodles += 50
      }
    }
    return { noodles: noodles, sauce: sauce}
  }
  
  export function addSecretIngredient(friendsList, myList) {
    let ingredient = friendsList[friendsList.length - 1]
    myList.push(ingredient)
  }
  
  export function scaleRecipe(recipe, portions) {
    let copyOfRecipe = {...recipe}
    for(let value in copyOfRecipe) {
      copyOfRecipe[value] = copyOfRecipe[value] / 2
      copyOfRecipe[value] = copyOfRecipe[value] * portions
    }
    return copyOfRecipe
  }