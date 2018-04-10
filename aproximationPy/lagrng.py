class Lagrng:
    """class finds aproximated value for x using LaGrange formula, takes points xp, yp as an input"""

    # input points values x, y
    __xvalues = []
    __yvalues = []

    # number of points entered
    __numPoints = 0

    # init for given points
    def __init__(self, points):
        self.__xvalues = list(points.keys())
        self.__yvalues = list(points.values())
        self.__numPoints = len(points)

    # finds aproximated value for x using LaGrange formula
    def lagrng_aprox_function(self, x):
        aprox_value = 0.0
        points_range = range(0, self.__numPoints)

        for i in points_range:
            basic_polinom = 1.0
            for j in points_range:
                if i != j:
                    basic_polinom *= (x - self.__xvalues[j])/(self.__xvalues[i] - self.__xvalues[j])
            aprox_value += basic_polinom * self.__yvalues[i]

        return aprox_value
