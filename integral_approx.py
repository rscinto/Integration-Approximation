#global variables

#accuracy
EPSILON = 0.0001
#slices of the interval per whole number 
# (b-a) * COLUMNS
COLUMNS = 1000000
#fixes decimal drift 
ADJUSTER = 100



#function called in New_Interval_Square class
def squareFunction( var ):
    return var**2

class New_Interval_Square:
        def __init__(self, start, stop, deltaX):
            self.start = start
            self.stop = stop
            self.mid = float((start+stop) / 2.0)
            self.area = float(squareFunction(self.mid) *  deltaX)
#end class New_Interval
    
class Approx_Integral:

    #CTOR
    def __init__(self, userStart, userStop):
        
        #initial conditions set for subInterval Creation
        self.parentStartInterval = userStart
        self.parentStopInterval = userStop
        self.n = float(userStop - userStart)
        self.nPlus = float(self.n * COLUMNS)
        self.deltaX = float(self.n / self.nPlus)
        self.totalArea = 0.0

        #Function call calulates the 
        self.riemannSum()

    def riemannSum(self):

        #priming reads set 
        start = self.parentStartInterval
        epsilon = EPSILON
        stop = start + epsilon
        
        while (stop < self.parentStopInterval):
            #subinterval are created 
            subINTERVAL = New_Interval_Square(start, stop, self.deltaX)

            #running total area 
            self.totalArea = subINTERVAL.area + self.totalArea

            #algorithm reset
            start = stop
            stop = stop + epsilon
        
        #this is a bandaid
        self.totalArea = self.totalArea * ADJUSTER
#end class Approx_Integral

#main
integralOne = Approx_Integral(0, 1)
print('Integral Approx of 0 to 1 of f(x) = x**2 dx: ', integralOne.totalArea)

integralTwo = Approx_Integral(0, 2)
print('Integral Approx of 0 to 2 of f(x) = x**2 dx: ', integralTwo.totalArea)

integralTwo = Approx_Integral(0, 4)
print('Integral Approx of 0 to 4 of f(x) = x**2 dx: ', integralTwo.totalArea)

integralTwo = Approx_Integral(0, 16)
print('Integral Approx of 0 to 16 of f(x) = x**2 dx: ', integralTwo.totalArea)

#here is a test 