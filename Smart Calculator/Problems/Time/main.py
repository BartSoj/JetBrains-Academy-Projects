class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def from_string(cls, time):
        hour, minute = time.split(":")
        return cls(hour, minute)
