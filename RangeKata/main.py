def OverlapsRN(range1,range2):
    R1 = Range(range1)
    R2 = Range(range2)
    R3 = Range.OverLapsRange(R1,R2)
    return  R3
def EqualNum(range1,range2):
    R1 = Range(range1)
    R2 = Range(range2)
    R3 = Range.EqualRanges(R1, R2)
    return R3

def ContainsRN(range1,range2):
    R1 = Range(range1)
    R2 = Range(range2)
    R3 = Range.ContainsRange(R1,R2)
    return R3
def EndPointsRN(range):
    R1 = Range(range)
    R2 = Range.Endpoint(R1)
    return R2
class Range:
    def __init__(self, Range):
        self.range = Range

    def ContainsRange(self,other):
        FirstNumber = int(self.range[1])
        LastNumber = int(self.range[-2])
        FirstNumber1 = int(other.range[1])
        LastNumber1 = int(other.range[-2])
        if self.range[0] == '(':
            FirstNumber = FirstNumber + 1
        if self.range[-1] == ')':
            LastNumber = LastNumber - 1
        if other.range[0] == '(':
            FirstNumber1 = FirstNumber1 + 1
        if other.range[-1] == ')':
            LastNumber1 = LastNumber1 - 1

        if FirstNumber1 >= FirstNumber and LastNumber1 <= LastNumber:
            return True
        else:
            return False

    def EqualRanges(self,other):
        FirstNumber = int(self.range[1])
        LastNumber = int(self.range[-2])
        FirstNumber01 = int(other.range[1])
        LastNumber01 = int(other.range[-2])
        if self.range[0] == '(':
            FirstNumber = FirstNumber + 1
        if self.range[-1] == ')':
            LastNumber = LastNumber - 1
        if other.range[0] == '(':
            FirstNumber01 = FirstNumber01 + 1
        if other.range[-1] == ')':
            LastNumber01 = LastNumber01 - 1

        if FirstNumber == FirstNumber01 and LastNumber == LastNumber01:
            return True
        else:
            return False

    def Endpoint(self):
        if self.range[0] == '(':
            FirstNumber = int(self.range[1]) + 1
        else:
            FirstNumber = int(self.range[1])
        if self.range[-1] == ')':
            LastNumber = int(self.range[-2]) -1
        else:
            LastNumber = int(self.range[-2])
        result = str(FirstNumber)+','+str(LastNumber)
        return result


    def OverLapsRange(self, other):
        if self.range[0] == '(':
         FirstNumber = int(self.range[1]) + 1
        else:
         FirstNumber = int(self.range[1])

        if self.range[-1] == ')':
            LastNumber = int(self.range[-2]) -1
        else:
            LastNumber = int(self.range[-2])

        if other.range[0] == '(':
            FirstNumber02 = int(other.range[1]) + 1
        else:
            FirstNumber02 = int(other.range[1])

        if other.range[-1] == ')':
            LastNumber02 = int(other.range[-2]) - 1
        else:
            LastNumber02 = int(other.range[-2])

        if FirstNumber <= FirstNumber02 <= LastNumber:
            return True
        elif FirstNumber <= LastNumber02 <= LastNumber:
            return True
        else:
            return False






if __name__ == '__main__':
    print('PyCharm')
