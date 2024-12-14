const pizzas = { "Margherita": 7, "Caprese": 9, "Formaggio": 10 }

export function pizzaPrice(pizza, ...extras) {
  const extra = [...extras]
  let total = 0
  for (let item of extra) {
    if (item == "ExtraSauce") {
      total += 1
    }
    else {
      total += 2
    }
  }
  return pizzas[pizza] + total
}

export function orderPrice(pizzaOrders) {
  let total = 0;
  for (let order of pizzaOrders) {
    const pizza = order.pizza;
    const extras = order.extras || [];

    total += pizzaPrice(pizza, ...extras);
  }
  return total;
}