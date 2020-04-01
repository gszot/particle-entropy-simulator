from Ball import Ball
from Calcs import *
from Point import P
from Sectors import *
from plot import plot2d


class Board:
    def __init__(self, r, R, N, c, W, acc, dtime, sectors_xy_number, sectors_vxy_number, iterations):
        self.balls = []
        sector1 = SectorXY(P(0, 0), P(0, 0))
        sector2 = SectorVXY(P(0, 0), P(0, 0))
        self.sectors_xy = [[sector1 for _ in range(sectors_xy_number)] for _ in range(sectors_xy_number)]
        self.sectors_vxy = [[sector2 for _ in range(sectors_vxy_number)] for _ in range(sectors_vxy_number)]
        self.r = r
        self.R = R
        self.N = N
        self.c = c
        self.W = W
        self.acc = acc * r
        self.dtime = dtime
        self.iterations = iterations
        self.sectors_xy_number = sectors_xy_number
        self.sectors_vxy_number = sectors_vxy_number
        self.sector_xy_size = 2 * R / sectors_xy_number
        self.sector_vxy_size = 2 * W / sectors_vxy_number
        self.M = sectors_xy_number ** 2 * sectors_vxy_number ** 2
        self.sectors_ns = []
        self.marked = []
        self.file = None
        self.data = ""

    def fill(self):
        d = 2 * self.R / (self.N + 1)
        for i in range(1, self.N + 1):
            x = -self.R + self.sector_xy_size / 2
            y = -self.R + i * d
            self.balls.append(Ball(x, y, self.N, self.c, self.W))

    def add_sectors(self):
        self.add_sectors_xy()
        self.add_sectors_vxy()
        self.add_sectors_ns()

    def add_sectors_xy(self):
        d = self.sector_xy_size
        for i in range(self.sectors_xy_number):
            for j in range(self.sectors_xy_number):
                ld = P(-self.R + j * d, -self.R + i * d)
                pg = P(-self.R + (j + 1) * d, -self.R + (i + 1) * d)
                self.sectors_xy[i][j] = SectorXY(ld, pg)

    def add_sectors_vxy(self):
        d = self.sector_vxy_size
        for i in range(self.sectors_vxy_number):
            for j in range(self.sectors_vxy_number):
                ld = P(-self.W + j * d, -self.W + i * d)
                pg = P(-self.W + (j + 1) * d, -self.W + (i + 1) * d)
                self.sectors_vxy[i][j] = SectorVXY(ld, pg)

    def add_sectors_ns(self):
        for i in range(self.sectors_xy_number):
            for j in range(self.sectors_xy_number):
                for k in range(self.sectors_vxy_number):
                    for l in range(self.sectors_vxy_number):
                        self.sectors_ns.append(SectorNS(self.sectors_xy[i][j], self.sectors_vxy[k][l]))

    def update(self):
        self.marked = []
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                if dist(self.balls[i], self.balls[j]) <= 2 * self.r + self.acc:
                    self.balls[i], self.balls[j] = ball_collision_ods(self.balls[i], self.balls[j], self.r, self.acc)

        for ball in self.balls:
            ball.vx, ball.vy = wall_collision(ball, self.R)
            ball.update()

    def update_sectors(self):
        for i in range(self.sectors_xy_number):
            for j in range(self.sectors_xy_number):
                self.sectors_xy[i][j].update(self)
        for i in range(self.sectors_vxy_number):
            for j in range(self.sectors_vxy_number):
                self.sectors_vxy[i][j].update(self)
        for sector in self.sectors_ns:
            sector.update(self)

    def throw_in(self):  # czasami jakaś wypada to wrzucam spowrotem
        for ball in [ball for ball in self.balls if ball not in self.marked]:
            ball.x = random.uniform(-self.R, self.R)
            ball.y = random.uniform(-self.R, self.R)

    def print_xy(self):
        for i in range(self.sectors_xy_number - 1, -1, -1):
            string = ""
            for j in range(self.sectors_xy_number):
                string += str(self.sectors_xy[i][j])
            print(string)

    def print_vxy(self):
        for i in range(self.sectors_vxy_number - 1, -1, -1):
            string = ""
            for j in range(self.sectors_vxy_number):
                string += str(self.sectors_vxy[i][j])
            print(string)

    def print_xy_count(self):
        suma = 0
        for i in range(self.sectors_xy_number - 1, -1, -1):
            string = ""
            for j in range(self.sectors_xy_number):
                string += str(self.sectors_xy[i][j].count) + " "
                suma += self.sectors_xy[i][j].count
        print("suma xy: ", suma)

    def print_vxy_count(self):
        suma = 0
        for i in range(self.sectors_vxy_number - 1, -1, -1):
            string = ""
            for j in range(self.sectors_vxy_number):
                string += str(self.sectors_vxy[i][j].count) + " "
                suma += self.sectors_vxy[i][j].count
        print("suma vxy: ", suma)

    def print_balls(self):
        string = ""
        for ball in self.balls:
            string += str(ball) + " "
        print(string)

    def prepare(self):
        self.fill()
        self.add_sectors()
        self.update_sectors()

    def next_iter(self):
        self.update()
        self.update_sectors()
        self.throw_in()

    def simulate(self):
        clock = 0
        self.file = open(self.data, "w")
        X, Y = update_data(self.N, self.file, clock, self, [], [])
        for i in range(self.iterations):
            self.next_iter()
            print(i, len(self.marked))
            clock += self.dtime
            X, Y = update_data(self.N, self.file, clock, self, X, Y)

        plot2d(X, Y)
        self.file.close()
