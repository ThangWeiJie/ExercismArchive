/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

/** 
  * @param {number | null} remainingTime
  * @returns {string} message
*/

export function cookingStatus(remainingTime = null) {
  if(remainingTime === null) {
    return 'You forgot to set the timer.';
  }
  
  if(remainingTime === 0) {
    return 'Lasagna is done.';
  } else {
    return 'Not done, please wait.';
  }
}

export function preparationTime(layers, averageTime = 2) {
  return layers.length * averageTime;
}

/** 
  * @param {string[]} layers
  * @returns {Quantity<string, number>} quantity object
*/

export function quantities(layers) {
  let noodle_gram = 0;
  let sauce_liter = 0;

  for(let i = 0; i < layers.length; i++) {
    if(layers[i] == 'sauce') {
      sauce_liter += 0.2;
    } else if(layers[i] == 'noodles') {
      noodle_gram += 50;
    }
  }

  return {
    noodles: noodle_gram,
    sauce: sauce_liter,
  };
}

/** 
  * @param {string[]} recipe1
  * @param {string[]} recipe2
  * @returns {string[]} updated recipe
*/

export function addSecretIngredient(recipe1, recipe2) {
  console.log(recipe1);
  console.log(recipe2);
  
  recipe2.push(recipe1[recipe1.length - 1]);
}

/** 
  * @param {Recipe<string, number>} recipe
  * @param {number} portion
  * @returns {Recipe<string, number>} scaled recipe
*/

export function scaleRecipe(recipe, portion) {
  let scaledRecipe = {};

  for(let key in recipe) {
    scaledRecipe[key] = recipe[key] * portion / 2;
  }

  return scaledRecipe;
}
