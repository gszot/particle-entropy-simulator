from Board import Board


def main():
    # ładnie r=0.1 R=15 N=100 c=1 W=10 dtime=1 acc=0.01*r xy=10 vxy=5 iterations=500
    r = 0.1  # promien kulki
    R = 15  # 'promień' pola
    N = 100  # ilość kulek     N*r < R !!!
    c = 1  # constant
    W = 10  # losowanie prędkości z przedziału (-W/c*N,W/c*N)
    acc = 0.01 * r  # dokładnosc odbicia ( 0 -> 2r )
    dtime = 1  # kwant czasu
    sectors_xy_number = 10  # ile sektorów w poziomie i pionie
    # sector_xy_size = 2 * R / sectors_xy_number
    sectors_vxy_number = 5  # ile sektorów w poziomie i pionie
    # sector_vxy_size = 2 * W / sectors_vxy_number
    # M = sectors_xy_number ** 2 * sectors_vxy_number ** 2

    iterations = 475
    data = "dane.txt"

    board = Board(r, R, N, c, W, acc, dtime, sectors_xy_number, sectors_vxy_number, iterations)
    board.data = data
    board.prepare()
    board.simulate()


if __name__ == '__main__':
    main()
