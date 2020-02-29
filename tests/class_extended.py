class example:
    def __init__(self, v):
        self.value = v

    def __add__(self, other):
        return example(self.value+other.value)

    def __sub__(self, other):
        return example(self.value-other.value)

    def __mul__(self, other):
        return example(self.value*other.value)

    def __truediv__(self, other):
        return example(self.value/other.value)

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return str(self.value)


    def __contains__(self, item):
        if isinstance(item, str):
            return True
        return False

    @property
    def prop(self):
        return self.value

    @prop.setter
    def prop(self,new):
        if new > 5:
            self.value = new


a = example(5)
b = example(6)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a.prop)
a.prop = 4
print(a.prop)
a.prop = 6
print(a.prop)

if "string" in a:
    print("yes")
if 1 in a:
    print("no")