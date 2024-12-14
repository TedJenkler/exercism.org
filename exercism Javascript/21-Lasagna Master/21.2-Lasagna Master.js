export function cookingStatus(time) {
    if (time === undefined) {
      return 'You forgot to set the timer.';
    } else if (time === 0) {
      return 'Lasagna is done.';
    } else if (typeof time === 'number' && time > 0) {
      return 'Not done, please wait.';
    } else {
      return 'Invalid time input.';
    }
  }
  
  export function preparationTime(layers, time = 2) {
    return layers.length * time
  }
  
  export function quantities(layers) {
    let sauce = 0;
    let noodles = 0;
  
    for (let item of layers) {
      if (item === "sauce") {
        sauce += 0.2;
      } else if (item === "noodles") {
        noodles += 50;
      }
    }
  
    return { "noodles": noodles, "sauce": sauce };
  }
  
  export function addSecretIngredient(array1, array2) {
    array2.push(array1[array1.length - 1]);
  }
  
  export function scaleRecipe(recipe, portions) {
    let copyOfRecipe = {...recipe}
    for (let item in copyOfRecipe) {
      copyOfRecipe[item] /= 2
      copyOfRecipe[item] *= portions
    }
    return copyOfRecipe
  }