
# if you want call this module (file) like any other python module you can do that by store this \
# file directory (package) at sys.path (sys.path.append('{this directory}')

class Calc:


    def __init__(self, first, second):      # __init__ is a constructor, when an object is generated it will be called automatically.
        self.first = first                  # self.first, self.second <-- object variable
        self.second = second                 


    def add(self):
        result = self.first + self.second
        return result


    def sub(self):
        result = self.first - self.second
        return result


    def div(self):
        try:
            result = self.first / self.second
        except ZeroDivisionError: 
            print(f"\n\nError : You are trying to divide {self.first} by 0\n\n")
            #print(e) #if you want to know the error message
            #pass #avoiding the error
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def power(self):
        result = self.first ** self.second
        return result

class MyError(Exception):
    def __str__(self):                      # this method shows the error message
        return "It's not allow to use that ID"
def say_nick(nick):
    if nick == "idiot":
        raise MyError()
    print(nick)



class MoreCalc(Calc):                       # MoreArithmaticCalc class gets inheritance from ArithmaticCalc class \
    pass                                    # it is useful when we want to edit class (e.g., class from library)


PI = 3.141592
class Math:
    def SurfaceCircle(self, r):
        return PI * (r ** 2)


if __name__ == "__main__":                    # proceed if the file is executed directly (__name__ stores __main__). 
    a = Calc(4, 2)                            # Thus, when we call this file as a module it won't proceed to the next sentences \
    print(a.div())                            # (__name__ stores {file name or module name})

    say_nick("Angel")
    say_nick("idiot")
