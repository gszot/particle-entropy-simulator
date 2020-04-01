import math

from Calcs import gen_velocity
from Point import P


class Ball(P):
    def __init__(self, x, y, N, c, W):
        P.__init__(self, x, y)
        self.vx, self.vy = gen_velocity(N, c, W)
        self.v = math.sqrt(self.vx ** 2 + self.vy ** 2)

    def update(self, dtime = 1):
        self.x += dtime * self.vx
        self.y += dtime * self.vy
        self.v = math.sqrt(self.vx ** 2 + self.vy ** 2)