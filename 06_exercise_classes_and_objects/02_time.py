class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        result = ''
        if self.hours < 10:
            result += f'0{self.hours}:'
        else:
            result += f'{self.hours}:'

        if self.minutes < 10:
            result += f'0{self.minutes}:'
        else:
            result += f'{self.minutes}:'

        if self.seconds < 10:
            result += f'0{self.seconds}'
        else:
            result += f'{self.seconds}'

        return result

    def next_second(self) -> str:
        if self.seconds < Time.max_seconds:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < Time.max_minutes:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours < Time.max_hours:
                    self.hours += 1
                else:
                    self.hours = 0

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
