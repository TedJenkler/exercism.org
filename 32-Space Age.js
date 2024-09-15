export const age = (planet, ageInSeconds) => {
    let ageInDays = ageInSeconds / 60 / 60 / 24;
    let ageInYears = Math.round(ageInDays / 365.25 * 100) / 100;
    let mercuryYears = Math.round(ageInDays / (365.25 * 0.2408467) * 100) / 100;
    let venusYears = Math.round(ageInDays / (365.25 * 0.61519726) * 100) / 100;
    let marsYears = Math.round(ageInDays / (365.25 * 1.8808158) * 100) / 100;
    let jupiterYears = Math.round(ageInDays / (365.25 * 11.862615) * 100) / 100;
    let saturnYears = Math.round(ageInDays / (365.25 * 29.447498) * 100) / 100;
    let uranusYears = Math.round(ageInDays / (365.25 * 84.016846) * 100) / 100;
    let neptuneYears = Math.round(ageInDays / (365.25 * 164.79132) * 100) / 100;
    
    switch(planet) {
      case 'earth':
        return ageInYears;
      case 'mercury':
        return mercuryYears;
      case 'venus':
        return venusYears;
      case 'mars':
        return marsYears;
      case 'jupiter':
        return jupiterYears;
      case 'saturn':
        return saturnYears;
      case 'uranus':
        return uranusYears;
      case 'neptune':
        return neptuneYears;
    }
  };