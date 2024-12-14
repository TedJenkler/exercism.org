import { notify } from './notifier';
import { order } from './grocer';

export function onSuccess() {
  return notify({ message: 'SUCCESS' })
}

export function onError() {
  return notify({ message: 'ERROR' })
}

export function orderFromGrocer(query, onSuccessCallback, onErrorCallback) {
  return order(query, onSuccessCallback, onErrorCallback)
}

export function postOrder(variety, quantity) {
  let data = { "quantity": quantity, "variety": variety }
  return order(data, onSuccess, onError)
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