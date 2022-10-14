class TestMath:
    def test_add(self,x,y):
        x=10
        y=10
        return x+y
    def test_subtract(self,x,y):
        x=10
        y=10
        return x-y
    def test_multiply(self,x,y):
        x=10
        y=10
        return x*y
    def test_divide(self,x,y):
        x=10
        y=10
        return x/y

# DRY(Don't Repeat Yourself) IMPLEMENTATION
class DryedTestMath:
    def __init__(self):
        self.x=10
        self.y=10

    def test_add(self):
        return self.x+self.y
    def test_subtract(self):
        return self.x-self.y
    def test_multiply(self):
        return self.x*self.y
    def test_divide(self):
        return self.x/self.y