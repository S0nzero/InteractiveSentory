from scipy.stats import sem, t
from scipy import mean


class HitDetector:
    pastValuesList = []
    confidence = 0
    threshold = 30.0
    intervals = 15

    def __init__(self, threshold, intervals):
        self.threshold = threshold
        self.intervals = intervals

    def confidence_interval(self):
        n = len(self.pastValuesList)
        m = mean(self.pastValuesList)
        std_err = sem(self.pastValuesList)
        h = std_err * t.ppf((1 + self.confidence) / 2, n - 1)
        return m-(h+10), m+(h+10)

    def new_value(self, new):
        self.confidence = self.new_confidence(0.95, 0.99)
        if len(self.pastValuesList) < 7:
            self.pastValuesList.append(new)
            return False
        else:
            st, end = self.confidence_interval(), 15
            if new > end and new > self.threshold:
                self.pastValuesList = []
                return True
            else:
                if len(self.pastValuesList) == 15:
                    self.pastValuesList = self.pastValuesList[1:]
                self.pastValuesList.append(new)
                return False

    def new_confidence(self, min_value, max_value):
        return max_value-(((max_value - min_value)/self.intervals)*len(self.pastValuesList))


HD = HitDetector(50, 15)
while True:
    HD.new_value(float(input("Rentrez votre valeur !")))
    if HD.pastValuesList:
        print(HD.confidence_interval())
        print(HD.confidence)
    print(HD.pastValuesList)
