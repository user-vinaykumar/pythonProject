import time


class Gadiyaara:

    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def dating(self):
        return self.y, self.m, self.d


    @classmethod
    def fromtimestamp(cls, ti):
        y, m, d, h, mi, sec, weekday, jday, jst = time.localtime(ti)
        return cls(y, m, d)

    @classmethod
    def today(cls):
        t = time.time()
        return cls.fromtimestamp(t)
m = time.time()
mm = Gadiyaara.fromtimestamp(m)
print(mm.dating())