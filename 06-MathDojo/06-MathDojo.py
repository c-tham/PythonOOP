class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *nums):
        for num in nums:
            self.result += num
        return self
    def subtract(self, *nums):
        for num in nums:
            self.result -= num
        return self

md = MathDojo()
print md.add(2).result
md = MathDojo()
print md.add(2,5).result
md = MathDojo()
print md.subtract(3,2).result

print "---->1"
md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result

class MathDojo2(MathDojo):
    def add(self, *nums):
        for num in nums:
            if type(num) == int:
                self.result += num
            if type(num) == list:
                for listnum in num:
                    self.result += listnum
        return self
    def subtract(self, *nums):
        for num in nums:
            if type(num) == int:
                self.result -= num
            if type(num) == list:
                for listnum in num:
                    self.result -= listnum
        return self

md2 = MathDojo2()
print md2.add([1,2]).result

print "---->2"
md2 = MathDojo2()
print md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result

class MathDojo3(MathDojo2):
    def add(self, *nums):
        for num in nums:
            if type(num) == int:
                self.result += num
            if type(num) == list:
                for listnum in num:
                    self.result += listnum
            if type(num) == tuple:
                for tuplenum in num:
                    self.result += tuplenum
                    # print self.result
        return self
    def subtract(self, *nums):
        for num in nums:
            if type(num) == int:
                self.result -= num
            if type(num) == list:
                for listnum in num:
                    self.result -= listnum
            if type(num) == tuple:
                for tuplenum in num:
                    self.result -= tuplenum
        return self


print "---->3"
md3 = MathDojo3()
print md3.add((1,2)).result
print "---->3"
md3 = MathDojo3()
print md3.add((1,2),[1,2],1).result
print "---->3"
md3 = MathDojo3()
print md3.subtract((1,2),[1,2],1).result