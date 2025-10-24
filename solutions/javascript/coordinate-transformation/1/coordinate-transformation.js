// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Create a function that returns a function making use of a closure to
 * perform a repeatable 2d translation of a coordinate pair.
 *
 * @param {number} dx the translate x component
 * @param {number} dy the translate y component
 *
 * @returns {function} a function which takes an x, y parameter, returns the
 *  translated coordinate pair in the form [x, y]
 */
export function translate2d(dx, dy) {
  let translatedPoint = [];
  const translation = (x, y) => {
    translatedPoint[0] = x + dx;
    translatedPoint[1] = y + dy;
    return translatedPoint;
  }
  return translation;
}

/**
 * Create a function that returns a function making use of a closure to
 * perform a repeatable 2d scale of a coordinate pair.
 *
 * @param {number} sx the amount to scale the x component
 * @param {number} sy the amount to scale the y component
 *
 * @returns {function} a function which takes an x, y parameter, returns the
 *  scaled coordinate pair in the form [x, y]
 */
export function scale2d(sx, sy) {
  let scaledPoint = [];
  function scale(x, y) {
    scaledPoint[0] = x * sx;
    scaledPoint[1] = y * sy;
    return scaledPoint;
  }

  return scale;
}

/**
 * Create a composition function that returns a function that combines two
 * functions to perform a repeatable transformation
 *
 * @param {function} f the first function to apply
 * @param {function} g the second function to apply
 *
 * @returns {function} a function which takes an x, y parameter, returns the
 *  transformed coordinate pair in the form [x, y]
 */
export function composeTransform(f, g) {
  function composedFunction(x, y) {
    let inner = f(x, y);
    return g(inner[0], inner[1]);
  }

  return composedFunction;
}

/**
 * Return a function that memoizes the last result.  If the arguments are the same as the last call,
 * then memoized result returned.
 *
 * @param {function} f the transformation function to memoize, assumes takes two arguments 'x' and 'y'
 *
 * @returns {function} a function which takes x and y arguments, and will either return the saved result
 *  if the arguments are the same on subsequent calls, or compute a new result if they are different.
 */
export function memoizeTransform(f) {
  let prevX;
  let prevY;
  let prevResult;

  function memoized(x, y) {
    if(prevX == x && prevY == y) {
      return prevResult;
    }

    prevX = x;
    prevY = y;
    prevResult = f(x, y);
    return prevResult;
  }

  return memoized;
}
