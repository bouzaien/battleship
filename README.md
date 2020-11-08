## Repository Setup
1. Install Miniconda, follow https://docs.conda.io/en/latest/miniconda.html

2. Create a fresh conda environment, and install all dependencies.

```text
conda create -n battleship python=3.8
conda activate battleship
git clone --recursive https://github.com/bouzaien/battleship.git
cd battleship
pip install -r requirements.txt
```

3. Install this codebase as a package in this environment.
```
python setup.py install --user
```


## Play a Game

To play a game, use the `src/play.py` script. Add `--show_positions` argument to show the ships positions during the game.

```text
python src/play.py --show_positions
```


## Simulate a Game

To simulate a game, use the `src/simulate.py` script. Add `--update_rate <value>` argument to set the figure update rate value. Default value is 0.5 seconds.

```text
python src/simulate.py --update_rate 0.5
```


## Generate Data

To generate data, use the `src/generate_data.py` script.

```text
python src/generate_data.py --games <num_games> --output_folder <folder> --file_name <file>
```

Example

```text
python src/generate_data.py --games 1000 --output_folder data --file_name generated_data
```

## Test Functionalities
To perform unit tests, use the `src/test.py` without any parameters.

```text
python tests/test.py
```