export function dayRate(ratePerHour) {
    return ratePerHour * 8;
  }
  
  export function daysInBudget(budget, ratePerHour) {
    const dailyRate = ratePerHour * 8;
    return Math.floor(budget / dailyRate);
  }
  
  export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
    const daysPerMonth = 22;
    const dailyRate = ratePerHour * 8;
    const monthlyRate = dailyRate * daysPerMonth;
    const discountedMonthlyRate = monthlyRate * (1 - discount);
  
    const fullMonths = Math.floor(numDays / daysPerMonth);
    const remainingDays = numDays % daysPerMonth;
  
    const totalCost = (fullMonths * discountedMonthlyRate) + (remainingDays * dailyRate);
    
    return Math.ceil(totalCost);
  }