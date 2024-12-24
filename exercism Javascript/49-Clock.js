export class Clock {
    constructor(hour = 0, minute = 0) {
      this.hour = hour;
      this.minute = minute;
      this.time = this.normalize();
    }
    
    normalize() {
      while (this.minute < 0) {
        this.minute += 60;
        this.hour -= 1;
      }
  
      while (this.minute >= 60) {
        this.minute -= 60;
        this.hour += 1;
      }
  
      while (this.hour < 0) {
        this.hour += 24;
      }
  
      this.hour %= 24;
  
      return this.formatTime();
    }
  
    formatTime() {
      const formattedHour = this.hour.toString().padStart(2, "0");
      const formattedMinute = this.minute.toString().padStart(2, "0");
      return `${formattedHour}:${formattedMinute}`;
    }
  
    toString() {
      return this.time;
    }
  
    plus(minutes) {
      this.minute += minutes;
      this.time = this.normalize();
      return this.time;
    }
  
    minus(minutes) {
      this.minute -= minutes;
      this.time = this.normalize();
      return this.time;
    }
  
    equals(other) {
      return this.time === other.time;
    }
  }