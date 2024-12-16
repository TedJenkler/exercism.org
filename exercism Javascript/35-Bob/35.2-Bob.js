export const hey = (message) => {
    let clean = message.trim().split("")
    let check = clean.filter((item) => /^[a-zA-Z]+$/.test(item)).length != 0
    if (clean[clean.length - 1] == "?" && message === message.toUpperCase() && check) {
      return "Calm down, I know what I'm doing!"
    }
    else if (clean[clean.length - 1] == "?") {
      return "Sure."
    }
    else if (message === message.toUpperCase() && check) {
      return "Whoa, chill out!"
    }
    else if (clean.length === 0) {
      return "Fine. Be that way!"
    }else {
      return "Whatever." 
    }
  };