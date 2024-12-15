export function isValidCommand(command) {
    return /^chatbot/i.test(command)
  }
  
  export function removeEmoji(message) {
    return message.replace(/\bemoji\d+\b/g, "");
  }
  
  export function checkPhoneNumber(number) {
    if (/^\(\+\d{2}\) \d{3}-\d{3}-\d{3}$/.test(number)) {
      return "Thanks! You can now download me to your phone."
    }else {
      return `Oops, it seems like I can't reach out to ${number}`
    }
  }
  
  export function getURL(userInput) {
    const regex = /\b(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})\b/g;
    const matches = userInput.match(regex);
    
    if (matches) {
      return matches.map(match => match.replace(/^(https?:\/\/)?(www\.)?/, ''));
    }
    
    return null;
  }
  
  export function niceToMeetYou(fullName) {
    return fullName.replace(/(\w+), (\w+)/, (match, lastName, firstName) => {
      return `Nice to meet you, ${firstName} ${lastName}`;
    });
  }