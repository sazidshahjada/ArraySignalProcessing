from mathmodels import CATARCSModel
from utils import compute_difference_coarray, prepare_grid, visualize_consecutive_lags


if __name__ == "__main__":
    # Define parameters for the CATARCS model
    M, N = 4, 5 # Coprime integers
    d = 1  # Inter-element spacing (normalized units)

    # Create an instance of the CATARCS model
    catarcs_model = CATARCSModel(M, N, d)

    # Get sensor positions
    sensor_positions = catarcs_model.sensor_positions()
    print("Sensor Positions:", sensor_positions)

    # Compute the difference coarray
    coarray = compute_difference_coarray(sensor_positions)
    print("Difference Coarray:", coarray)

    # Prepare the grid for visualization
    range_value = 40  # Define the range for the grid
    grid = prepare_grid(range_value, coarray)

    # Visualize the consecutive lags
    visualize_consecutive_lags(
        grid, ncols=10, save=True,
        save_path='figures/consecutive_lags_CATARCS_visualization.png',
        show=True
        )