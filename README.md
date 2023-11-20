# Hermes - Genetic Algorithm for the Traveling Salesman Problem

This project, developed with FastAPI, addresses the Traveling Salesman Problem (TSP) using a genetic algorithm approach to find efficient routes. The backend connects with a user interface implemented in the repository [Hermes](https://github.com/jiChicojt/Hermes).


![Resultado Final](https://i.postimg.cc/TP1pmQtw/Hermes.png)

## Summary

This system focuses on solving the TSP, a classic optimization challenge, through genetic algorithms. The file `main.py` contains the FastAPI server logic that processes route requests. On the other hand, `geneticAlgorithm.py` implements the genetic algorithm used to find optimal routes.

## Key Functions and Implementation

### `main.py`
- **Route Calculation:** Processes route requests sent from the user interface.
- **CORS Connection:** Configures CORS policies to allow access from `localhost`.

### `geneticAlgorithm.py`
- **Conversion to Distances:** Converts output routes into distances for processing.
- **Random Route Generation:** Creates random routes from available locations and connections.
- **Route Evaluation:** Calculates route effectiveness considering distance, time, and complexity.
- **Genetic Algorithm:** Implements the evolutionary process, including selection, crossover, and mutation.

## Usage

To use this project, ensure that you have FastAPI, Pydantic, and Uvicorn installed.

## Execution

1. Install dependencies by running:
    ```bash
    pip install fastapi~=0.104.1 pydantic~=2.5.1 uvicorn~=0.24.0.post1
    ```
2. Run the server with:
    ```bash
    uvicorn main:app --reload
    ```
## Contributions

Feel free to contribute to this project by forking it and creating a pull request with your improvements. All contributions are welcome and appreciated!

Explore and enjoy route optimization with this genetic algorithm for the TSP!
