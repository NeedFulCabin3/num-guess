# Num Guess

> Terminal-based integer evaluation runtime with interactive input boundary validation.

## Overview

Interactive CLI tools often break when processing unexpected non-numeric input types or out-of-bounds user guesses. `num-guess-cli` demonstrates standard input-sanitization patterns in terminal interfaces. It isolates stream extraction from game mechanics to prevent crashes during continuous interactive loops, serving as a clean reference for fault-tolerant console control flows.

## How It Works

The engine relies on a blocking event loop anchored in CPython's standard library.

```text
+----------------------------------------------------------------+
|                         main() Loop                            |
|                                                                |
|  1. Generate random integer via random.randint(1, 100)         |
|  2. Initialize attempt counter = 0                             |
|                                                                |
|  +----------------------------------------------------------+  |
|  |                get_valid_integer() Loop                  |  |
|  |                                                          |  |
|  |  [stdin] ---> int(input()) ---> Success?                 |  |
|  |                  |                 |                     |  |
|  |                 No                Yes                    |  |
|  |                  |                 |                     |  |
|  |             Catch ValueError       v                     |  |
|  |             Print message     Return integer             |  |
|  |             Loop again                                   |  |
|  +----------------------------------------------------------+  |
|                               |                                |
|                               v                                |
|  3. Increment attempt counter                                  |
|  4. Evaluate relative range (guess < lower or guess > upper)   |
|     ---> If Out-of-Bounds: Warn & skip evaluation loop         |
|  5. Compare guess against target                               |
|     ---> If Low / High: Print hint & continue loop             |
|     ---> If Match: Print total attempts & break loop           |
+----------------------------------------------------------------+
```


1. **Random Value Generation**: Uses CPython's `random.randint` (derived from the Mersenne Twister PRNG) to select a secret integer within target parameters.
2. **Input Stream Handling**: Wraps `input()` calls inside a dedicated validation function (`get_valid_integer`). String inputs are cast to base-10 integers inside a `try...except ValueError` block. Unparseable inputs trigger immediate recovery messaging without unwinding the stack.
3. **Boundary Verification**: Evaluates parsed integers against range conditions (`lower_bound`, `upper_bound`) before evaluating equality. Out-of-bounds inputs generate dynamic feedback without consuming valid strategic attempts.
4. **State Machine Terminal Transition**: Evaluates high/low conditions via branching logic (`if/elif/else`). Matching conditions report accumulated execution counts and trigger a controlled loop break.

## Key Features

* **Isolated Parsing Strategy**: Input sanitization logic resides outside primary execution logic to maintain single-responsibility separation.
* **Fault-Tolerant Input Stream**: Handled `ValueError` exceptions ensure malformed user entries do not cause unhandled program termination.
* **Dynamic Boundary Checks**: Range limits validate inputs before testing target values, maintaining data validity throughout execution.
* **Execution Count Tracking**: Incrementing state counter persists total evaluated attempts across loop iterations.

## Tech Stack & Core Dependencies Breakdown

* **Language**: Python 3.10+
* **Standard Library Modules**:
  * `random`: Core pseudo-random integer generation algorithm (`randint`). No external dependencies required.

## Environment & Web-Based Quick Start

### Running in GitHub Codespaces

1. Click the **Code** button at the top of the repository web interface.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. Once the web terminal initializes, execute the application directly:
   ```bash
   python main.py
   ```

## Local Virtual Environment

```text
# Clone repository
git clone [https://github.com/your-username/num-guess-cli.git](https://github.com/your-username/num-guess-cli.git)
cd num-guess-cli

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Run application
python main.py
```

## Repository Structure

```text
num-guess-cli/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow for linting, typing, and tests
├── .gitignore              # Environment and runtime file exclusion rules
├── LICENSE                 # MIT Open-Source License
├── README.md               # Architecture documentation and usage guide
└── main.py                 # Core engine entrypoint and validation loops
```

## Roadmap

[ ] **Configurable Difficulty Ranges:** Pass range parameters (--min, --max) directly via command-line interface arguments using argparse.

[ ] **Automated Unit Testing:** Implement unit tests using pytest to validate parser handling of edge cases and non-numeric characters.

[ ] **Structured Dynamic Output:** Migrate standard terminal outputs to rich library formatting to render colored feedback and attempt counters.
