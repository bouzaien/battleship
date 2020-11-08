import argparse

from Battleship import Battleship

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--size", type=int, 
        default=10, 
        help="Field size"
    )

    parser.add_argument(
        "--show_positions",
        action="store_true",
        help="Whether to show ships positions while playing",
    )

    args = parser.parse_args()

    # create a game instance and start playing
    bs = Battleship(field_size=(args.size,args.size))
    bs.play(show_positions=args.show_positions)

if __name__ == "__main__":
    main()