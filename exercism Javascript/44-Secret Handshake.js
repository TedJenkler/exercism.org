let command = ["wink", "double blink", "close your eyes", "jump", "reverse"];

export const commands = (num) => {
  let result = [];
  let binary = num.toString(2).padStart(5, "0").split("").reverse();

  for (let i = 0; i < 4; i++) {
    if (binary[i] === "1") {
      result.push(command[i]);
    }
  }

  if (binary[4] === "1") {
    result.reverse();
  }

  return result
};