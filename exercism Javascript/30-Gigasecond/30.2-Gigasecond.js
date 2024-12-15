export const gigasecond = (date) => {
    const newDate = new Date(date);
    newDate.setSeconds(newDate.getSeconds() + 1000000000);
    return newDate;
  };