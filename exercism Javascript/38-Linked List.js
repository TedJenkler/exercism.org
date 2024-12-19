export class Node {
    constructor(value) {
      this.value = value
      this.next = null
      this.prev = null
    }
  }
  
  export class LinkedList {
    constructor() {
      this.head = null
      this.tail = null
      this.size = 0
    }
    push(value) {
      const newNode = new Node(value);
      if(!this.head) {
        this.head = this.tail = newNode;
      }else {
        this.tail.next = newNode;
        newNode.prev = this.tail;
        this.tail = newNode;
      }
      this.size++
      return value
    }
  
    pop() {
    if (!this.tail) return null;
      
    const value = this.tail.value;
      
    if (this.head === this.tail) {
      this.head = this.tail = null;
    } else {
      this.tail = this.tail.prev;
      this.tail.next = null;
    }
  
    this.size--;
    return value;
  }
  
    shift() {
      if(!this.head) return null;
  
      const value = this.head.value
  
      if(this.head === this.tail) {
        this.head = this.tail = null;
      }else {
        this.head = this.head.next
        this.head.prev = null
      }
      this.size--;
      return value
    }
  
    unshift(value) {
      const newNode = new Node(value);
      if(!this.head) {
        this.head = this.tail = newNode;
      }else {
        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode;
      }
      this.size++
    }
  
    delete(value) {
      let current = this.head;
  
      while (current) {
        if (current.value === value) {
          if (current === this.head && current === this.tail) {
            this.head = this.tail = null;
          }
          else if (current === this.head) {
            this.head = this.head.next;
            this.head.prev = null;
          }
          else if (current === this.tail) {
            this.tail = this.tail.prev;
            this.tail.next = null;
          }
          else {
            current.prev.next = current.next;
            current.next.prev = current.prev;
          }
  
          this.size--;
          return;
        }
  
        current = current.next;
      }
    }
  
    count() {
      return this.size
    }
  }