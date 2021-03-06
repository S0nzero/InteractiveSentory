from scipy.stats import sem, t
from scipy import mean


class HitDetectorManager:
    HitDetectorList = []
    numberSensors = 0
    lastButtonHit = None

    def __init__(self, number_sensors, threshold, intervals):
        self.numberSensors = number_sensors
        self.HitDetectorList = []
        for i in range(number_sensors):
            self.HitDetectorList.append(HitDetector(threshold, intervals))

    def new_value(self, result):
        hit_detected = False
        for i in range(len(result)):
            if self.HitDetectorList[i].new_value(int(result[i])):
                hit_detected = True
                self.lastButtonHit = i
        return hit_detected

    def print_values(self):
        for i in self.HitDetectorList:
            print(i.pastValuesList)


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
            st, end = self.confidence_interval()
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
