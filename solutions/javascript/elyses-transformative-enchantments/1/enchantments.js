// @ts-check

/**
 * Double every card in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with every card doubled
 */
export function seeingDouble(deck) {
  const doubledDeck = deck.map(value => value * 2);
  return doubledDeck;
}

/**
 *  Creates triplicates of every 3 found in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with triplicate 3s
 */
export function threeOfEachThree(deck) {
  const duped = deck.reduce(
    (accumulator, currentValue) => {
        if(currentValue === 3) {
            accumulator.newDeck.push(currentValue);
            accumulator.newDeck.push(currentValue);
            accumulator.newDeck.push(currentValue);
        } else {
            accumulator.newDeck.push(currentValue);
        }

        return accumulator;
    }, {newDeck: []}
);

    return duped.newDeck;
}

/**
 * Extracts the middle two cards from a deck.
 * Assumes a deck is always 10 cards.
 *
 * @param {number[]} deck of 10 cards
 *
 * @returns {number[]} deck with only two middle cards
 */
export function middleTwo(deck) {
  return deck.slice(4, 6);
}

/**
 * Moves the outside two cards to the middle.
 *
 * @param {number[]} deck with even number of cards
 *
 * @returns {number[]} transformed deck
 */

export function sandwichTrick(deck) {
  const len = deck.length;
  const firstElement = deck[0];
  const lastElement = deck[len - 1];

  deck.splice(len / 2, 0, lastElement);
  deck.pop();

  deck.splice(len / 2 + 1, 0, firstElement);
  deck.shift();

  return deck;
}

/**
 * Removes every card from the deck except 2s.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with only 2s
 */
export function twoIsSpecial(deck) {
  return deck.filter(value => value === 2);
}

/**
 * Returns a perfectly order deck from lowest to highest.
 *
 * @param {number[]} deck shuffled deck
 *
 * @returns {number[]} ordered deck
 */
export function perfectlyOrdered(deck) {
  const compareFunction = (value1, value2) => {
    if(value1 < value2) {return -1;}
    if(value1 > value2) {return 1;}
    return 0;
  }

  return deck.sort(compareFunction);
}

/**
 * Reorders the deck so that the top card ends up at the bottom.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} reordered deck
 */
export function reorder(deck) {
  return deck.reverse();
}
