import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def tinh_chu_vi(self):
        return self.a + self.b + self.c
    
    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    

class TamGiacVuong(TamGiac):
    def __init__(self, a):
        super().__init__(a, a, math.sqrt(2) * a)
    

class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, b)


class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)