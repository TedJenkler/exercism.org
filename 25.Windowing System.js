export class Size {
    constructor(width = 80, height = 60) {
      this.width = width
      this.height = height
    }
  
    resize(newWidth, newHeight) {
      this.width = newWidth
      this.height = newHeight
    }
  }
  
  export class Position {
    constructor(x = 0, y = 0) {
      this.x = x
      this.y = y  
    }
  
    move(newX, newY) {
      this.x = newX
      this.y = newY
    }
  }
  
  export class ProgramWindow {
    constructor() {
      this.screenSize = new Size(800, 600);  
      this.size = new Size();  
      this.position = new Position();
    }
    resize(newSize) {
      let maxWidth = this.screenSize.width - this.position.x;
      let maxHeight = this.screenSize.height - this.position.y;
      let newWidth = Math.max(1, Math.min(newSize.width, maxWidth));
      let newHeight = Math.max(1, Math.min(newSize.height, maxHeight));
      this.size.resize(newWidth, newHeight);
    }
    move(newPosition) {
      let newX = Math.min(Math.max(newPosition.x, 0), this.screenSize.width - this.size.width);
      let newY = Math.min(Math.max(newPosition.y, 0), this.screenSize.height - this.size.height);
      this.position.move(newX, newY);
    }
  }
  
  export function changeWindow(programWindow) {
    const newSize = new Size(400, 300);
    programWindow.resize(newSize);
  
    const newPosition = new Position(100, 150);
    programWindow.move(newPosition);
  
    return programWindow;
  }