from mathmodels import GoldenRatioModel
from utils import compute_difference_coarray, prepare_grid, visualize_consecutive_lags


if __name__ == "__main__":
    # Define parameters for the CATARCS model
    M, N = 3, 4 # Coprime integers
    d = 1  # Inter-element spacing (normalized units)

    # Create an instance of the models
    golden_ratio_model = GoldenRatioModel(M, N, d)
    
    # Get sensor positions
    sensor_positions = golden_ratio_model.sensor_positions()
    print("Number of Sensors:", golden_ratio_model.number_of_sensors)
    print("Degrees of Freedom:", golden_ratio_model.dof)
    print("Sensor Positions:", sensor_positions)
    # Compute the difference coarray
    coarray = compute_difference_coarray(sensor_positions)
    print("\nDifference Coarray:", coarray)

    # Prepare the grid for visualization
    range_value = 50  # Define the range for the grid
    grid = prepare_grid(range_value, coarray)

    # Visualize the consecutive lags
    visualize_consecutive_lags(
        grid, ncols=10, save=True,
        save_path='figures/consecutive_lags_goldenratio_visualization.png',
        show=True
        )
    

