# ArraySignalProcessing

This repository provides Python implementations of advanced array signal processing techniques for Direction of Arrival (DOA) estimation using sparse array configurations.

## Features

- **CATARCS Model**: Implementation of the CATARCS sparse array model for sensor placement.
- **Difference Coarray Calculation**: Compute the difference coarray from sensor positions.
- **Visualization Tools**: Visualize consecutive lags and coarray coverage using matplotlib.

## File Structure

- `mathmodels.py`: Contains the [`CATARCSModel`](mathmodels.py) class for generating sensor positions.
- `utils.py`: Utility functions for coarray computation and visualization, including [`compute_difference_coarray`](utils.py), [`prepare_grid`](utils.py), and [`visualize_consecutive_lags`](utils.py).
- `experiment.py`: Example script demonstrating the use of the CATARCS model and visualization tools.
- `README.md`: Project documentation.

## Usage

1. **Install dependencies**:
    ```sh
    pip install numpy pandas matplotlib
    ```

2. **Run the experiment**:
    ```sh
    python experiment.py
    ```

This will print the sensor positions, the difference coarray, and display a visualization of the consecutive lags.

## Example

The default experiment uses coprime integers `M=4`, `N=5` and normalized spacing `d=1`. You can modify these parameters in [`experiment.py`](experiment.py).

## License

MIT License