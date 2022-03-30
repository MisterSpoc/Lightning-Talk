import fire

def helloWorld(text):
    print("Hello {}".format(text))
    return
    
def dataTypes(inp):
    print(inp)
    print(type(inp))
    return
    
def returns(num):
    match num:
        case 0:
            return "String"
        case 1:
            return 1
        case 2:
            return 3.14
        case 3:
            return [0,1,2,3]
        case 4:
            return {'apple':2, 'orange':9.2, 'banana':-3}
        case 5:
            return (1,2,3,4)
    
def multipleInputs(number, str = 'Hello World'):
    print(number)
    print(str)
    return

def args(*args):
    return args

def kwargs(**kwargs):
    return kwargs

class Obj():
    def __init__(self):
        self.num1 = 2
        self.num2 = 5
        self.list = ["Apple", "Orange", "Banana"]
    
    def __str__(self):
        return 'num1: {}\nnum2: {}\nlist: {}'.format(self.num1, self.num2, self.list)
    
    def setNums(self, x, y):
        self.num1 = x
        self.num2 = y
        return self
    
    def setList(self, *args):
        self.list = list(args)
        return self
    
    def square(self):
        self.num1 = self.num1**2
        self.num2 = self.num2**2
        return self

if __name__ == '__main__':
    fire.Fire()