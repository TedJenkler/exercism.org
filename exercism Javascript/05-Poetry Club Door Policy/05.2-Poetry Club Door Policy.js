export function frontDoorResponse(line) {
    return line[0];
  }
  
  export function frontDoorPassword(word) {
    let str = word.toLowerCase();
    return str[0].toUpperCase() + str.slice(1)
  }
  
  export function backDoorResponse(line) {
    let trim = line.trim()
    return trim[trim.length - 1]
  }
  
  export function backDoorPassword(word) {
    return frontDoorPassword(word) + ", please"
  }