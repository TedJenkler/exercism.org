export function translate2d(dx, dy) {
    return function (x, y) {
      return [x + dx, y + dy];
    };
  }
  
  export function scale2d(sx, sy) {
    return function (x, y) {
      return [x * sx, y * sy];
    };
  }
  
  export function composeTransform(f, g) {
    return function (x, y) {
      const [x1, y1] = f(x, y);
      return g(x1, y1);
    };
  }
  
  export function memoizeTransform(fn) {
    let lastArgs = null;
    let lastResult = null;
  
    return function (...args) {
      if (lastArgs && args.length === lastArgs.length && args.every((arg, index) => arg === lastArgs[index])) {
        return lastResult;
      }
  
      lastArgs = args;
      lastResult = fn(...args);
      return lastResult;
    };
  }