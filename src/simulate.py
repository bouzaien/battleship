import argparse

from Battleship import Battleship

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--size", type=int, 
        default=10, 
        help="game field size"
    )

    parser.add_argument(
        "--update_rate", type=float, 
        default=0.5, 
        help="figure update rate"
    )

    args = parser.parse_args()

    # create a a game instance and start simulating 
    bs = Battleship(field_size=(args.size,args.size))
    bs.simulate(update_rate=args.update_rate)

if __name__ == "__main__":
    main()