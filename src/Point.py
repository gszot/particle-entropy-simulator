class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # return "("+str(self.x)+","+str(self.y)+")"
        return "(" + str(round(self.x, 2)) + "," + str(round(self.y, 2)) + ")"