const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

const slangs = { "first": 1, "second": 2, "third": 3, "fourth": 4 };

export const meetup = (year, month, string, daystring) => {
  let date = new Date(year, month - 1, 1);

  if (string === "teenth") {
    date.setDate(13);
    while (date.getMonth() === month - 1 && date.getDate() <= 19) {
      if (days[date.getDay()] === daystring) {
        return date;
      }
      date.setDate(date.getDate() + 1);
    }
  } else if (string === "last") {
    date = new Date(year, month, 0);
    while (date.getMonth() === month - 1) {
      if (days[date.getDay()] === daystring) {
        return date;
      }
      date.setDate(date.getDate() - 1);
    }
  } else if (slangs[string]) {
    const sameDay = [];

    while (date.getMonth() === month - 1) {
      if (days[date.getDay()] === daystring) {
        sameDay.push(new Date(date));
      }
      date.setDate(date.getDate() + 1);
    }

    const index = slangs[string] - 1;
    if (sameDay[index]) {
      return sameDay[index];
    } else {
      throw Error(`${string} ${daystring} does not exist in this month.`);
    }
  }

  throw Error("Invalid input or no match found.");
};