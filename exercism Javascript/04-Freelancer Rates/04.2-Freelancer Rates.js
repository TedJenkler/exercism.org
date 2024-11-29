export function dayRate(ratePerHour) {
    return ratePerHour * 8;
  }
  
  export function daysInBudget(budget, ratePerHour) {
    return Math.floor(budget / dayRate(ratePerHour));
  }
  
  export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
    let mRate = dayRate(ratePerHour) * 22;
    let discountedMRate = mRate * (1 - discount);
    let months = Math.floor(numDays / 22)
    let days = numDays % 22
    return Math.ceil((months * discountedMRate) + (days * dayRate(ratePerHour)))
  }