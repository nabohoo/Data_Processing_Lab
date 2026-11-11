# Data Processing Lab

This repository contains the code and data for the `data-processing-lab` Python project. It is designed to practice using Python `lambda` functions, sorting, and basic data processing workflows using Git.

## Project Structure

*   `data_processing.py`: The main Python script containing the data processing logic and lambda functions.
*   `Cities.csv`: The dataset used for processing.

## Objectives

1.  **Lambda Functions**: Practice writing and applying anonymous functions in Python for short, one-off operations.
2.  **Data Filtering and Sorting**: Use `lambda` with built-in functions like `sorted()` to manipulate and rank records.
3.  **Git Version Control**: Practice basic Git operations, including initializing a repository, staging files, and creating structured commits.

## Setup Instructions

1.  Initialize this repository locally:
    ```bash
    git init data-processing-lab
    cd data-processing-lab
    ```
2.  Ensure `data_processing.py` and `Cities.csv` are copied into this directory.
3.  Run the script to observe the initial output:
    ```bash
    python data_processing.py
    ```

## Development Tasks

### Commit 1: Initial Implementation
*   Open `data_processing.py` and complete the sections marked `"Your code here"`.
*   **Tasks include:**
    *   Writing a `triple` lambda function.
    *   Sorting a list of records `[("A", 72), ("B", 91), ("C", 85)]` by score using `sorted()` with a lambda.
    *   Writing a `boost(scores, rule)` function to adjust scores using a lambda that adds 10 but caps the score at 100.
*   Once complete, commit the changes:
    ```bash
    git add data_processing.py Cities.csv
    git commit -m "Initial commit for data processing code"
    ```

### Commit 2: Refactoring
*   Refactor the initial code to improve modularity by defining reusable functions, such as `filter_items(condition, dict_list)`.
