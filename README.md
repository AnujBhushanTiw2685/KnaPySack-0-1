# Knapsack Game

An educational 0/1 Knapsack solver and interactive game implemented in Python. The project demonstrates three algorithmic approaches (recursive, memoized, tabulation) in `knapsack.py` and provides a simple Tkinter-based GUI game (`gui.py`) where players try to select items to match the optimal knapsack value.

**Key Ideas**
- Educational demonstration of the 0/1 knapsack problem
- Three implementations: recursion, memoization (top-down), and tabulation (bottom-up)
- Interactive game that compares the player's selection to the optimal solution

**Repository Structure**

- `knapsack.py` — Knapsack implementations (`Knapsack` class)
- `main.py` — Small CLI test harness that prints solver outputs
- `gui.py` — Tkinter GUI: play the knapsack game interactively
- `README.md` — This file

## Features

- Compute optimal knapsack value using:
	- Plain recursion (`kpRec`)
	- Memoized recursion (`kpMem`)
	- Tabulation / dynamic programming (`kpTab`)
- Simple game UI with item selection, capacity checks, and final comparison to the optimal value

## Requirements

- Python 3.8+ (tested on Windows)
- `tkinter` (standard library GUI package; usually included with Python installs)

## Installation

1. Clone or download the repository.
2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. No additional packages required for the basic project — `tkinter` is included with CPython distributions. If `tkinter` is missing, install it using your platform package manager.

## Usage

Run the CLI test harness:

```powershell
python main.py
```

Expected example output for the shipped example data (weights `[1,3,4]`, values `[10,40,50]`, capacity `5`):

```
Recursive 60
Memoized 60
Tabulated 60
```

Run the GUI game:

```powershell
python gui.py
```

How the GUI works:
- A list of items with weight and value is shown.
- Click `Select` to pick an item (the UI prevents exceeding capacity).
- Click `Finalize Selection` to see your total value and compare it with the optimal value computed by the `Knapsack` solver.

## Implementation Details

The `Knapsack` class in `knapsack.py` exposes three main methods:

- `kpRec(n, W)` — naive recursive solution (exponential time)
- `kpMem(n, W)` — top-down memoized solution (uses `self.t` table)
- `kpTab()` — bottom-up dynamic programming (tabulation), returns optimal value for configured `n`, `W`, `wt`, `val`

Time complexity (tabulation / memoized): O(n * W). Space complexity: O(n * W) for the DP table.

## Customizing Inputs

To try different instances, edit the weight (`wt`), value (`val`), number of items (`n`) and capacity (`W`) variables in `main.py` or `gui.py`.

Example (in `main.py`):

```python
n = 3
W = 5
wt = [1,3,4]
val = [10,40,50]
```

## Development

- The code is small and self-contained — tests are manual via `main.py` or by running `gui.py`.
- If you add new features or change algorithms, keep the interface of `Knapsack` (constructor and solver methods) compatible to make testing easy.

## Contributing

Contributions are welcome. Please:

1. Fork the repo
2. Create a feature branch
3. Open a pull request with a clear description and example usage

## License

No license file is included in the repository. If you want to open-source this project, consider adding an `LICENSE` (for example, MIT) to make reuse terms explicit.

---


