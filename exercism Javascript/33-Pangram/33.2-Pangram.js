let alphabet = new Set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']);

export const isPangram = (word) => {
  let arr = word.toLowerCase().split("").filter((item) => /^[a-z]$/.test(item));
  return new Set(arr).size === alphabet.size
};