export function totalBirdCount(birdsPerDay) {
    let sum = 0
    for(let i = 0; i < birdsPerDay.length; i++) {
      sum += birdsPerDay[i]
    }
    return sum
  }
  
  export function birdsInWeek(birdsPerDay, week) {
    let sum = 0
    let end = 7 * week
    let start = end - 7
    
    for(let i = start; i < end; i++) {
      sum += birdsPerDay[i]
    }
    return sum
  }
  
  export function fixBirdCountLog(birdsPerDay) {
    for(let i = 0; i < birdsPerDay.length; i++) {
      if(i == 0) birdsPerDay[i] += 1
      else if(i % 2 === 0) birdsPerDay[i] += 1
    }
    return birdsPerDay
  }