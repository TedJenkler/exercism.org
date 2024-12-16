export const age = (planet, seconds) => {
    let minutes = seconds / 60
    let hours = minutes / 60
    let days = hours /  24
    let earthYears = Math.round(days / 365.25 * 100) / 100
    switch (planet) {
      case 'earth':
        return earthYears
      case 'mercury':
        return Math.round(earthYears / 0.2408467 * 100) / 100
      case 'venus':
        return Math.round(earthYears / 0.6155000 * 100) / 100
      case 'mars':
        return Math.round(earthYears / 1.8808158 * 100) / 100
      case 'jupiter':
        return Math.round(earthYears / 11.862615 * 100) / 100
      case 'saturn':
        return Math.round(earthYears / 29.447498 * 100) / 100
      case 'uranus':
        return Math.round(earthYears / 84.016846 * 100) / 100
      case 'neptune':
        return Math.round(earthYears / 164.79132 * 100) / 100
    }
  };