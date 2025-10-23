// @ts-check

/**
 * Generates a random starship registry number.
 *
 * @returns {string} the generated registry number.
 */
export function randomShipRegistryNumber() {
  let min = 1000;
  let max = 10000;  
  return `NCC-${Math.floor(Math.random() * (max - min) + min)}`;
}

/**
 * Generates a random stardate.
 *
 * @returns {number} a stardate between 41000 (inclusive) and 42000 (exclusive).
 */
export function randomStardate() {
  let min = 41000;
  let max = 42000;  
  return Math.random() * (max - min) + min;
}

/**
 * Generates a random planet class.
 *
 * @returns {string} a one-letter planet class.
 */
export function randomPlanetClass() {
  let planetaryClasses = ['D', 'H', 'J', 'K', 'L', 'M', 'N', 'R', 'T', 'Y'];
  let min = 0;
  let max = planetaryClasses.length;

  let randomIdx = Math.floor(Math.random() * (max - min) + min);
  return planetaryClasses[randomIdx];
}
