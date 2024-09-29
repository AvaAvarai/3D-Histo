import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def plot_3d_histogram(csv_file):
    # Load the CSV dataset
    data = pd.read_csv(csv_file)
    
    # Check if the dataset is valid
    if data.empty:
        print("The dataset is empty or invalid.")
        return
    
    # Extract column names
    column_names = data.columns
    
    # Create a 3D histogram plot for each feature on the isometric plane
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Bin and offset settings
    bins = 15  # Number of bins for histograms
    hist_width = 0.8  # Width of the histogram bars
    offset_gap = 2  # Gap between histogram slices
    
    # Iterate over each feature
    for i, feature_name in enumerate(column_names):
        # Ensure the column contains numerical data
        try:
            feature_data = data[feature_name].astype(float)
        except ValueError:
            print(f"Skipping non-numerical column: {feature_name}")
            continue
        
        # Calculate histogram data
        hist, bin_edges = np.histogram(feature_data, bins=bins)
        
        # Center bin edges
        bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
        
        # Create the histogram as a 3D bar plot
        ax.bar(bin_centers, hist, zs=offset_gap * i, zdir='y', alpha=0.8, width=hist_width, label=feature_name)
    
    # Set labels for the axes
    ax.set_xlabel('Feature Values')
    ax.set_ylabel('Feature Index (Separated)')
    ax.set_zlabel('Frequency')
    
    # Set the title and legend
    ax.set_title("3D Histogram View of CSV Dataset Features")
    ax.legend()
    
    # Show the plot
    plt.show()

def select_csv_file():
    # Use Tkinter's file dialog to pick a file
    Tk().withdraw()  # Prevents the Tkinter root window from appearing
    file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
    
    # Check if a file was selected
    if file_path:
        plot_3d_histogram(file_path)
    else:
        print("No file selected.")

# Call the file picker function to load and visualize the CSV dataset
select_csv_file()
