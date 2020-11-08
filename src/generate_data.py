import os

import argparse
import tqdm

from Battleship import *

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file_name", type=str, 
        default="generated_data", 
        help="Output folder"
    )
    
    parser.add_argument(
        "--output_folder", type=str, 
        default="data", 
        help="Output folder"
    )

    parser.add_argument(
        "--games", type=int, 
        default="1000", 
        help="Number of games simulated to generate data"
    )

    args = parser.parse_args()

    samples_list = list()
    answers_list = list()

    for _ in tqdm.tqdm(range(args.games)):
        bs = Battleship()
        states, answers = bs.genarateData()
        samples_list.append(states)
        answers_list.append(answers)
    
    # concatenate the samples of each played games to get a tuple of ()
    generated_data = (np.concatenate(samples_list, axis=0), np.concatenate(answers_list, axis=0))

    os.makedirs(args.output_folder, exist_ok=True)

    for data, Xy in zip(generated_data, ['X', 'y']):
        file_name = args.file_name + "_" + Xy + "_" + str(args.games) + ".npy"
        full_path = os.path.join(args.output_folder, file_name)
        np.save(full_path, data)
        print("File saved to {}".format(full_path))

if __name__ == "__main__":
    main()