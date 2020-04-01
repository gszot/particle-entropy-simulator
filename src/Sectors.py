class Sector:
    def __init__(self, ld, pg):  # lewy dolny, prawy górny klasy P
        self.ld = ld
        self.pg = pg
        self.count = 0


class SectorXY(Sector):
    def include(self, ball):
        if self.ld.x < ball.x < self.pg.x and self.ld.y < ball.y < self.pg.y:
            return True
        else:
            return False

    def update(self, board):
        self.count = 0
        for ball in board.balls:
            if self.include(ball):
                board.marked.append(ball)
                self.count += 1

    def __str__(self):
        return "(" + str(self.ld) + "," + str(self.pg) + ")"


class SectorVXY(Sector):
    def include(self, ball):
        if self.ld.x < ball.vx < self.pg.x and self.ld.y < ball.vy < self.pg.y:
            return True
        else:
            return False

    def update(self, board):
        self.count = 0
        for ball in board.balls:
            if self.include(ball):
                self.count += 1

    def __str__(self):
        return "(" + str(self.ld) + "," + str(self.pg) + ")"


class SectorNS:
    def __init__(self, sector_xy, sector_vxy):
        self.sector_xy = sector_xy
        self.sector_vxy = sector_vxy
        self.count = 0

    def update(self, board):
        self.count = 0
        for ball in board.balls:
            if self.sector_xy.include(ball) and self.sector_vxy.include(ball):
                self.count += 1