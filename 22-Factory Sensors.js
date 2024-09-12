export class ArgumentError extends Error {}

export class OverheatingError extends Error {
  constructor(temperature) {
    super(`The temperature is ${temperature} ! Overheating !`);
    this.temperature = temperature;
  }
}

export function checkHumidityLevel(humidityPercentage) {
  if (humidityPercentage > 70) {
    throw new Error();
  }
}

export function reportOverheating(temperature) {
  if (temperature === null) {
    throw new ArgumentError();
  } else if (temperature > 500) {
    throw new OverheatingError(temperature);
  }
}

export function monitorTheMachine(actions) {
  try {
    const temperature = actions.check();
  } catch (error) {
    if (error instanceof ArgumentError) {
      actions.alertDeadSensor();
    } else if (error instanceof OverheatingError) {
      if (error.temperature < 600) {
        actions.alertOverheating();
      } else {
        actions.shutdown();
      }
    } else {
      throw error;
    }
  }
}