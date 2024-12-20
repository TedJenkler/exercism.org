const operators = ["plus", "minus", "multiplied", "divided"]

const logic = {
  "plus": (a, b) => a + b,
  "minus": (a, b) => a - b,
  "multiplied": (a, b) => a * b,
  "divided": (a, b) => a / b
}

const restricted = ["cubed", "Who"]

const isValid = (cleaned) => {
  let valid = [];

  for (let item of cleaned.split(" ")) {
    if (restricted.includes(item)) {
      throw new Error("Unknown operation")
    }
    if (!isNaN(Number(item)) || operators.includes(item)) {
      valid.push(item);
    }
  }

  for (let i = 0; i < valid.length; i++) {
    if (i % 2 === 0) {
      if (isNaN(Number(valid[i]))) {
        throw new Error("Syntax error");
      }
    } else {
      if (!operators.includes(valid[i])) {
        throw new Error("Syntax error");
      }
    }
  }

  if (valid.length === 0 || isNaN(Number(valid[0])) || isNaN(Number(valid[valid.length - 1]))) {
    throw new Error("Syntax error");
  }
};

export const answer = (word) => {
  let cleaned = word.split("").filter((item) => !/[.,\/#!$%\^&\*;:{}=\?_`~()]/g.test(item)).join("");

  isValid(cleaned);

  let total = 0;
  let currentOperation = "plus"

  for (let item of cleaned.split(" ")) {
    if (operators.includes(item)) {
      currentOperation = item;
    } else if (!isNaN(Number(item))) {
      const num = Number(item);
      total = logic[currentOperation](total, num);
    }
  }

  return total;
};