export const gigasecond = (time) => {
    const GIGASECOND_IN_MS = 1000000000 * 1000;
    let newDate = new Date(time.getTime() + GIGASECOND_IN_MS);
    return newDate;
  };