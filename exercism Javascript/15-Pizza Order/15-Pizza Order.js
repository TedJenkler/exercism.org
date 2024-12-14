/**
 * Determine the price of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
export function pizzaPrice(pizza, ...extras) {
    let total = 0
    switch(pizza) {
      case 'Margherita':
        total += 7
      break;
      case 'Caprese':
        total += 9
      break;
      case 'Formaggio':
        total += 10
      break;
    }
  
    const arr = [...extras]
  
    for(let i = 0; i < arr.length; i++) {
      if(arr[i] === "ExtraSauce") {
        total += 1
      }else if (arr[i] === "ExtraToppings") {
        total += 2
      }
    }
    return total
  }
  
  /**
   * Calculate the price of the total order, given individual orders
   *
   * (HINT: For this exercise, you can take a look at the supplied "global.d.ts" file
   * for a more info about the type definitions used)
   *
   * @param {PizzaOrder[]} pizzaOrders a list of pizza orders
   * @returns {number} the price of the total order
   */
  export function orderPrice(pizzaOrders) {
    let totalPrice = 0;
  
    for (let i = 0; i < pizzaOrders.length; i++) {
      const order = pizzaOrders[i];
      const pizzaName = order.pizza;
      const extras = order.extras || [];
      totalPrice += pizzaPrice(pizzaName, ...extras)
    }
  
    return totalPrice;
  }