import fire

def helloWorld(text):
    """Prints "Hello <input text>"

    Args:
        text (str): a text string
    """
    print("Hello {}".format(text))
    return
    
def dataTypes(inp):
    """Prints the input value and its data type to the console

    Args:
        inp (Any): Any single input
    """
    print(inp)
    print(type(inp))
    return
    
def returns(num):
    """Returns various data types depending on input integer.
    Use to demonstrate how fire handles different data types in return statements

    Args:
        num (int): an integer in range(0,6)

    Returns:
        Any: one of a data type
    """
    match num:
        case 0:
            return "String"
        case 1:
            return 1.5
        case 2:
            return [0,1,2,3]
        case 3:
            return [[0,1,2,3],[1,2,3],['apple', 'orange', 8, 2]]
        case 4:
            return {'apple':2, 'orange':9.2, 'banana':5}
        case 5:
            return (1,2,3,4)
    
def multipleInputs(number, string = 'Hello World'):
    """*Returns input values.
    Use to demonstrate flags and multiple inputs in fire

    Args:
        number (int): any input.
        str (str, optional): any input. Defaults to 'Hello World'.
    """
    print(number)
    print(string)
    return

def args(*args):
    """*Returns input

    Returns:
        tuple: returns tuple of input values
    """
    return args

def kwargs(**kwargs):
    """Returns input

    Returns:
        dict: returns dictionary of input values
    """
    return kwargs

class Obj():
    """*Example object to demonstrate calling objects in fire
    """
    def __init__(self, num1=2, num2=5):
        self.num1 = num1
        self.num2 = num2
        self.list = ["Apple", "Orange", "Banana"]
    
    def __str__(self):
        return 'num1: {}\nnum2: {}\nlist: {}'.format(self.num1, self.num2, self.list)
    
    def setNums(self, x, y):
        """Use to set num1 and num2 Obj values

        Args:
            x (int,float): any number
            y (int,float): any number

        Returns:
            Obj: self
        """
        self.num1 = x
        self.num2 = y
        return self
    
    def setList(self, *args):
        """Use to set list Obj value

        Returns:
            Obj: self
        """
        self.list = list(args)
        return self
    
    def square(self):
        """Squares num1 and num2 and updates their values

        Returns:
            Obj: self
        """
        self.num1 = self.num1**2
        self.num2 = self.num2**2
        return self
    
    def half(self):
        """Halves num1 and num2 and updates their values

        Returns:
            Obj: self
        """
        self.num1 = self.num1/2
        self.num2 = self.num2/2
        return self
    

if __name__ == '__main__':
    fire.Fire()
    # fire.Fire(helloWorld)
    # fire.Fire({
    #     'data':dataTypes,
    #     'return':returns
    #            })