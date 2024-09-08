/**
 * @return void
 */
export function onSuccess() {
  return notify({ message: 'SUCCESS' }) 
}

/**
 * @return void
 */
export function onError() {
  return notify({ message: 'ERROR' }) 
}

/**
 * @param {GrocerQuery} query
 * @param {FruitPickerSuccessCallback} onSuccessCallback
 * @param {FruitPickerErrorCallback} onErrorCallback
 * @return void
 */
export function orderFromGrocer(query, onSuccessCallback, onErrorCallback) {
  return order(query, onSuccess, onErrorCallback)
}

/**
 * @param {string} variety
 * @param {number} quantity
 * @return void
 */
export function postOrder(variety, quantity) {
  const query = {
    variety, 
    quantity
  }
  return order(query, onSuccess, onError)
}





/**
 * @param {FruitPickerSuccess | FruitPickerError} message
 * @return void
 */
export function notify(message) {
  // This is a mocked function for use with the exercise.
  message;
}





/**
 * @param {GrocerQuery} query
 * @param {GrocerOnSuccessCallback} onSuccess
 * @param {GrocerOnErrorCallback} onError
 * @return void
 */
export function order(query, onSuccess, onError) {
  // This is a mocked function for use with the exercise.
  query;
  onSuccess;
  onError;
}