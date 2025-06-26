import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def compute_difference_coarray(sensor_positions):
    lags = []
    for i in sensor_positions:
        for j in sensor_positions:
            lags.append(i - j)
    coarray = np.array(lags)
    coarray = np.unique(coarray)
    return coarray

def prepare_grid(range, coarray):
    grid = {"Positions": [], "IsCovered": []}
    space = np.arange(-range, range + 1)
    for pos in space:
        grid["Positions"].append(pos)
        if np.abs(pos) in coarray:
            grid["IsCovered"].append(True)
        else:
            grid["IsCovered"].append(False)
    
    grid = pd.DataFrame(grid)
    return grid

def visualize_consecutive_lags(grid, ncols=10, title='Consecutive Lags Visualization'):
    neg_grid = grid[grid['Positions'] < 0].sort_values('Positions', ascending=False)
    zero_grid = grid[grid['Positions'] == 0]
    pos_grid = grid[grid['Positions'] > 0].sort_values('Positions')
    
    ncols_neg = ncols
    ncols_pos = ncols
    
    nrows_neg = int(np.ceil(len(neg_grid) / ncols_neg))
    nrows_pos = int(np.ceil(len(pos_grid) / ncols_pos))
    nrows = max(nrows_neg, nrows_pos)
    
    total_cols = ncols_neg + 1 + ncols_pos
    
    fig, ax = plt.subplots(figsize=(20, nrows * 1.2))  # Adjusted height based on rows
    
    circle_radius = 0.4
    cell_size = 1.0
    
    for i, (pos, covered) in enumerate(zip(neg_grid['Positions'], neg_grid['IsCovered'])):
        row = i // ncols_neg
        col = ncols_neg - 1 - (i % ncols_neg)
        center_x = col * cell_size
        center_y = row * cell_size
        facecolor = 'green' if covered else 'red'
        circle = Circle((center_x, center_y), circle_radius, facecolor=facecolor, edgecolor='black')
        ax.add_patch(circle)
        text_color = 'black' if covered else 'white'
        ax.text(center_x, center_y, str(pos), ha='center', va='center', color=text_color, fontsize=16)
    
    for i, (pos, covered) in enumerate(zip(pos_grid['Positions'], pos_grid['IsCovered'])):
        row = i // ncols_pos
        col = i % ncols_pos + ncols_neg + 1
        center_x = col * cell_size
        center_y = row * cell_size
        facecolor = 'green' if covered else 'red'
        circle = Circle((center_x, center_y), circle_radius, facecolor=facecolor, edgecolor='black')
        ax.add_patch(circle)
        text_color = 'black' if covered else 'white'
        ax.text(center_x, center_y, str(pos), ha='center', va='center', color=text_color, fontsize=16)
    
    if not zero_grid.empty:
        zero_pos = zero_grid['Positions'].iloc[0]
        zero_covered = zero_grid['IsCovered'].iloc[0]
        center_x = ncols_neg * cell_size
        center_y = 0
        facecolor = 'green' if zero_covered else 'red'
        circle = Circle((center_x, center_y), circle_radius, facecolor=facecolor, edgecolor='black')
        ax.add_patch(circle)
        text_color = 'black' if zero_covered else 'white'
        ax.text(center_x, center_y, str(zero_pos), ha='center', va='center', color=text_color, fontsize=16)
    
    ax.set_xlim(-0.5 * cell_size, (total_cols - 0.5) * cell_size)
    ax.set_ylim((nrows - 0.5) * cell_size, -0.5 * cell_size)  # Reversed y-axis to place zero at top
    ax.set_aspect('equal')  # Ensure aspect ratio preserves circle shapes
    
    ax.hlines(np.arange(0, nrows * cell_size, cell_size), -0.5 * cell_size, (total_cols - 0.5) * cell_size, color='gray', linewidth=0.5)
    ax.vlines(np.arange(0, total_cols * cell_size, cell_size), -0.5 * cell_size, (nrows - 0.5) * cell_size, color='gray', linewidth=0.5)
    
    ax.set_title(title, fontsize=16)
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.tight_layout()
    plt.show()
