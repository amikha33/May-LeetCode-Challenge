class Solution:
    def checkStraightLine(self, coordinates):

             #IF JUST TWO COORDINATES, THEY WILL ALWAYS BE ON A LINE
            if len(coordinates) <= 2:
                return True

            #IF GRADIENT IS INFINITE, MEANING FIRST TWO FORM A VERTICAL LINE
            if coordinates[0][0] == coordinates[1][0]:
                for point in coordinates:
                    if point[1] != coordinates[0][0]:
                        return False

            #ALL OTHER CASES
            else:
                gradient = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
                yIntercept = coordinates[0][1] - (gradient * coordinates[0][0])
                for point in coordinates:
                    if point[1] != ((gradient * point[0]) + yIntercept):
                        return False
            return True
