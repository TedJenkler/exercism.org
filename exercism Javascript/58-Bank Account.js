export class BankAccount {
    constructor() {
      this.state = "not started";
      this._balance = 0;
    }
  
    delay(ms) {
      const start = Date.now();
      while (Date.now() - start < ms) {}
    }
  
    open() {
      if (this.state !== "open") {
        this.state = "open";  
        this._balance = 0
      }else {
        throw new ValueError() 
      }
    }
  
    close() {
      if (this.state == "open") {
        this.state = "closed";  
      }else {
        throw new ValueError() 
      }
    }
  
    deposit(amount) {
      if (this.state !== "open" || typeof amount !== "number" || amount <= 0) {
        throw new ValueError()
      }
      this.delay(2)
      this._balance += amount
    }
  
    withdraw(amount) {
      if (this.state !== "open" || typeof amount !== "number" || amount <= 0 || amount > this._balance) {
        throw new ValueError()
      }
  
      this.delay(2);
      this._balance -= amount;
    }
  
    get balance() {
      if (this.state == "open") {
        return this._balance
      }else {
        throw new ValueError()
      }
    }
  }
  
  export class ValueError extends Error {
    constructor() {
      super('Bank account error');
    }
  }