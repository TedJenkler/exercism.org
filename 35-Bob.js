export const hey = (message) => {
    let trimMsg = message.trim() 
    if(trimMsg.toUpperCase() === trimMsg && trimMsg[trimMsg.length - 1] === "?" && trimMsg.match(/[a-zA-Z]/)) {
      return "Calm down, I know what I'm doing!"
    }
    if(trimMsg[trimMsg.length - 1] === "?"){
      return "Sure."
    }
    if(trimMsg.toUpperCase() === trimMsg && trimMsg.match(/[a-zA-Z]/)) {
      return "Whoa, chill out!" 
    }
    if(trimMsg === "") {
      return "Fine. Be that way!"
    }
    return "Whatever."
  };