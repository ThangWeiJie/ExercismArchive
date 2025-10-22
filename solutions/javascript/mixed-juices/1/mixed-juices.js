// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  switch(name) {
    case 'Pure Strawberry Joy':
      return 0.5;
      break;
    case 'Energizer':
    case 'Green Garden':
      return 1.5;
      break;
    case 'Tropical Island':
      return 3;
      break;
    case 'All or Nothing':
      return 5;
      break;
    default:
      return 2.5;
      break;
  }
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {
  let currentWedges = 0;
  let numCuts = 0;

  const smallLime = 6;
  const mediumLime = 8;
  const largeLime = 10;
  
  while(numCuts <= limes.length) {
    if(currentWedges >= wedgesNeeded) {
      return numCuts;
    }

    let currLime = limes[numCuts];
    numCuts++;

    switch(currLime) {
      case 'small':
        currentWedges += smallLime;
        break;
      case 'medium':
        currentWedges += mediumLime;
        break;
      case 'large':
        currentWedges += largeLime;
        break;
    }
  }

  return numCuts - 1;
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  while(timeLeft > 0) {
    timeLeft -= timeToMixJuice(orders[0]);
    orders.shift();
  }

  return orders;
}
