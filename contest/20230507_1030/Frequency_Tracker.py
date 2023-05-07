# This is the failed one
class FrequencyTracker:

    def __init__(self):
        self.dict_ = {}

    def add(self, number: int) -> None:
        if number in self.dict_.keys():
            self.dict_[number] += 1
        else :
            self.dict_[number] = 1
        print(self.dict_)

    def deleteOne(self, number: int) -> None:
        if number in self.dict_.keys() and self.dict_[number] > 0:
            self.dict_[number] -= 1
        print(self.dict_)

    def hasFrequency(self, frequency: int) -> bool:
        print(frequency in self.dict_.values())