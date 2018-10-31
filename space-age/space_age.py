
def formatter(func):
    def wrapper(self):
        return float(f'{func(self): .2f}')
    return wrapper


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth = (self.seconds / 86400) / 365.25

    @formatter
    def on_earth(self):
        return self.earth

    @formatter
    def on_mercury(self):
        return (self.earth / 0.2408467)

    @formatter
    def on_venus(self):
        return (self.earth / 0.61519726)

    @formatter
    def on_mars(self):
        return (self.earth / 1.8808158)

    @formatter
    def on_jupiter(self):
        return (self.earth / 11.862615)

    @formatter
    def on_saturn(self):
        return (self.earth / 29.447498)

    @formatter
    def on_uranus(self):
        return (self.earth / 84.016846)

    @formatter
    def on_neptune(self):
        return (self.earth / 164.79132)

    # def __format__(self, format_spec):
    #     return self.__format__(format_spec)




