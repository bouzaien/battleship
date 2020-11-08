## Repository Setup

Create a fresh conda environment, and install all dependencies.

```text
conda create -n battleship python=3.8
conda activate battleship
git clone --recursive https://github.com/bouzaien/battleship.git
cd battleship
pip install -r requirements.txt
```


## Play a Game

To play a game, use the `src/play.py` script. Add `--show_position` argument to show the ships positions during the game.

```text
python src/play.py --show_position
```


## Simulate a Game

To simulate a game, use the `src/simulate.py` script.


## Generate Data

To generate data, use the `src/generate_data.py` script.

```text
python src/generate_data.py --games <num_games> --output_folder <folder> --file_name <file>
```

Example

```text
python src/generate_data.py --games 1000 --output_folder data --file_name generated_data
```