class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.normalize_time()
    
    def normalize_time(self):
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        self.hour = self.hour % 24
        if self.hour < 0:
            self.hour += 24


    def __repr__(self):
         return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def add_minutes(self, minutes):
        self.minute += minutes
        self.normalize_time()
    
    def __add__(self, minutes):
        new_clock = Clock(self.hour, self.minute)
        new_clock.add_minutes(minutes)
        return new_clock

    def subtract_minutes(self, minutes):
        self.minute -= minutes
        self.normalize_time()

    def __sub__(self, minutes):
        new_clock = Clock(self.hour, self.minute)
        new_clock.subtract_minutes(minutes)
        return new_clock