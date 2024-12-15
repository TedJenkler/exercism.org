export class Size {
    constructor(width = 80, height = 60) {
      this.width = width;
      this.height = height;
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
      const maxWidth = this.screenSize.width - this.position.x;
      const maxHeight = this.screenSize.height - this.position.y;
  
      const clippedWidth = Math.max(1, Math.min(newSize.width, maxWidth));
      const clippedHeight = Math.max(1, Math.min(newSize.height, maxHeight));
  
      this.size = new Size(clippedWidth, clippedHeight);
    }
  
    move(newPosition) {
      const maxX = this.screenSize.width - this.size.width;
      const maxY = this.screenSize.height - this.size.height;
  
      const clippedX = Math.max(0, Math.min(newPosition.x, maxX));
      const clippedY = Math.max(0, Math.min(newPosition.y, maxY));
  
      this.position = new Position(clippedX, clippedY);
    }
  }
  
  export function changeWindow(programWindow) {
    programWindow.resize(new Size(400, 300));
    programWindow.move(new Position(100, 150));
    return programWindow
  }