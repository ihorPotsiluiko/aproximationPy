class Mnq:
    """class finds polynomial constants using Gauss method, takes points x, y as an input"""

    # input values x, y: dictionary(key:x, value:y)
    __points = {}

    # polynomial constants for output eq.: a1 + a2*x + a3*x^2 + ...
    __a = []

    # number of points inputed
    __numPoints = 0

    # polinomial power for MNQ method
    __polPower = 3

    # rigth side of the matrix for Gauss method
    __xSums = []

    # left side of the matrix for Gauss method
    __b = []

    # init for given points and runs calculation
    def __init__(self, points):
        self.__points = points
        self.__numPoints = len(points)

        # create empty lists
        self.__xSums = [[0.0 for x in range(self.__polPower + 1)] for y in range(self.__polPower + 1)]
        self.__b = [0.0 for x in range(self.__polPower + 1)]
        self.__a = [0.0 for x in range(self.__polPower + 1)]

        self.__run_MNQ()

    # convert Gauss matrix to string for testing
    def __str_matrix(self):
        str = '\n __b {} xSums:'.format(self.__b)
        for i in range(len(self.__xSums)):
            str += '\n{}'.format(self.__xSums[i])
        return str

    # convert class data to string for testing
    def __str__(self):
        str = 'Метод найменших квадратів\npoints {}\nnumPoints {}\na {}' \
            .format(self.__points, self.__numPoints, self.__a)
        return str + self.__str_matrix()

    # create Gauss matrix
    def __initialise_gauss_matrix(self):
        xPoints = list(self.__points.keys())
        yPoints = list(self.__points.values())
        polinom_power_range = range(0, self.__polPower + 1)
        points_range = range(0, self.__numPoints)

        for i in polinom_power_range:
            for j in polinom_power_range:
                for k in points_range:
                    self.__xSums[i][j] += pow(xPoints[k], i + j)

        for i in polinom_power_range:
            for k in points_range:
                self.__b[i] += pow(xPoints[k], i) * yPoints[k]
        return

    # exchange rows if zero on diagonal
    def __make_diagonal_notzeros(self):
        polinom_power_range = range(0, self.__polPower + 1)

        for i in polinom_power_range:
            if self.__xSums[i][i] == 0:
                for j in polinom_power_range:
                    if i == j:
                        continue
                    if self.__xSums[j][i] != 0 and self.__xSums[i][j] != 0:
                        temp = self.__xSums[j]
                        self.__xSums[j] = self.__xSums[i]
                        self.__xSums[i] = temp

                        tempb = self.__b[j]
                        self.__b[j] = self.__b[i]
                        self.__b[i] = tempb
                        break
        return

    # transform matrix to diagonal view
    def __transform_matrix(self):
        for i in range(0, self.__polPower + 1):
            for j in range(i + 1, self.__polPower + 1):
                if (self.__xSums[i][i] == 0):
                    return False

                coef = self.__xSums[j][i] / self.__xSums[i][i]

                for k in range(i, self.__polPower + 1):
                    self.__xSums[j][k] -= coef * self.__xSums[i][k]

                self.__b[j] -= coef * self.__b[i]
        return True

    # calculate output constants a1, a2, ...
    def __calculate_constants(self):
        for i in range(self.__polPower, -1, -1):
            s = 0.0
            for j in range(i, self.__polPower + 1):
                s += self.__xSums[i][j] * self.__a[j]
            self.__a[i] = (self.__b[i] - s) / self.__xSums[i][i]
        return    

    # run MNQ method
    def __run_MNQ(self):
        if self.__polPower > self.__numPoints:
            return
        self.__initialise_gauss_matrix()
        # print(self.__str_matrix())
        self.__make_diagonal_notzeros()
        # print(self.__str_matrix())
        if self.__transform_matrix() == False:
            return
        # print(self.__str_matrix())
        self.__calculate_constants()
        # print('a = {}'.format(self.__a))
        return

    # calculate aproximated value for x
    def mnq_aprox_function(self, x):
        y = 0.0
        for i in range(len(self.__a)):
            y += self.__a[i] * pow(x, i)
        return y
