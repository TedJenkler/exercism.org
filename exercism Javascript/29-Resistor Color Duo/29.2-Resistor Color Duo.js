const COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

export const decodedValue = (colors) => {
  let result = 0
  let multi = 10
  for (let i = 0; i < 2; i++) {
    result += COLORS.indexOf(colors[i]) * multi
    multi = 1
  }
  return result
};