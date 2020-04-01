import copy
import math
import random
from decimal import Decimal


def gen_velocity(N, c, W):
    vx = random.uniform(-W / (c * N), W / (c * N))
    vy = random.uniform(-W / (c * N), W / (c * N))
    while vx == 0 or vy == 0:
        vx = random.uniform(-W / (c * N), W / (c * N))
        vy = random.uniform(-W / (c * N), W / (c * N))
    return vx, vy


def dist(b1, b2):
    return math.sqrt((b1.x - b2.x) ** 2 + (b1.y - b2.y) ** 2)


def dot(w1, w2):
    return w1[0] * w2[0] + w1[1] * w2[1]


def mag(w):
    return math.sqrt(w[0] ** 2 + w[1] ** 2)


def ball_collision_ods(b1, b2, r, acc):
    DIST = dist(b1, b2)
    w1 = [b1.x - b2.x, b1.y - b2.y]
    w2 = [b1.vx - b2.vx, b1.vy - b2.vy]
    b1c = copy.deepcopy(b1)
    b2c = copy.deepcopy(b2)
    roz_dist = abs(2 * r - DIST) / 2 + acc
    if mag(w1) < r * acc:
        w1short = [-x * roz_dist / b1.v for x in [b1.vx, b1.vy]]
        w2short = [-x * roz_dist / b2.v for x in [b2.vx, b2.vy]]
        b1.x += w1short[0]
        b1.y += w1short[1]
        b2.x += w2short[0]
        b2.y += w2short[1]
        c = dot(w1, w2) / dist(b1, b2) ** 2
    else:
        w1short = [x * roz_dist / mag(w1) for x in w1]
        mw1short = [-x for x in w1short]
        b1.x += w1short[0]
        b1.y += w1short[1]
        b2.x += mw1short[0]
        b2.y += mw1short[1]
        c = dot(w1, w2) / DIST ** 2
    dvx = c * (b2c.x - b1c.x)
    dvy = c * (b2c.y - b1c.y)
    b1.vx += dvx
    b1.vy += dvy
    b2.vx -= dvx
    b2.vy -= dvy
    return b1, b2


def wall_collision(ball, R):
    b = copy.deepcopy(ball)
    b.update()
    if b.y < -R or b.y > R:  # górna i dolna
        return b.vx, -b.vy
    elif b.x < -R or b.x > R:  # lewa i prawa
        return -b.vx, b.vy
    else:
        return b.vx, b.vy


def entropy(n, tablica_ns):
    suma = Decimal(0)
    for ns in tablica_ns:
        if ns.count != 0:
            suma += ns.count * Decimal(ns.count).ln() - ns.count
    s = Decimal(str((n * Decimal(n).ln() - n) - suma))
    return s


def praw_term(s):  # prawdopodobienstwo termodynamiczne
    return math.e ** s


def update_data(N, plik, clock, board, X, Y):
    en = entropy(N, board.sectors_ns)
    plik.writelines([str(clock) + " ", str(en) + "\n"])
    X.append(clock)
    Y.append(en)
    return X, Y
