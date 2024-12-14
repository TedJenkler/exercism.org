export function createVisitor(name, age, ticketId) {
    return {name: name, age: age, ticketId: ticketId}
  }
  
  export function revokeTicket(visitor) {
    visitor.ticketId = null
    return visitor
  }
  
  export function ticketStatus(tickets, ticketId) {
    if (ticketId in tickets && tickets[ticketId] !== null) {
      return `sold to ${tickets[ticketId]}`;
    } else if (tickets[ticketId] === null) {
      return 'not sold';
    } else {
      return 'unknown ticket id';
    }
  }
  
  export function simpleTicketStatus(tickets, ticketId) {
    if(tickets[ticketId] || tickets[ticketId] == '' && tickets[ticketId] !== null) {
      return tickets[ticketId]
    }
    else {
      return 'invalid ticket !!!'
    }
  }
  
  export function gtcVersion(visitor) {
    return visitor?.gtc?.version
  }