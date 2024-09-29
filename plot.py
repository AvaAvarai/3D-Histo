import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from matplotlib.widgets import Slider

def plot_3d_histogram(csv_file):
    # Load the CSV dataset
    data = pd.read_csv(csv_file)
    
    # Check if the dataset is valid
    if data.empty:
        print("The dataset is empty or invalid.")
        return
    
    # Extract column names, excluding the 'class' column
    column_names = [col for col in data.columns if col.lower() != 'class']
    
    # Create a figure and 3D axes
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Initial bin and offset settings
    initial_bins = 15
    hist_width = 0.8
    offset_gap = 2
    
    def update_plot(bins):
        ax.clear()
        
        # Iterate over each feature, excluding the 'class' column
        for i, feature_name in enumerate(column_names):
            # Ensure the column contains numerical data
            try:
                feature_data = data[feature_name].astype(float)
            except ValueError:
                print(f"Skipping non-numerical column: {feature_name}")
                continue
            
            # Calculate histogram data
            hist, bin_edges = np.histogram(feature_data, bins=int(bins))
            
            # Center bin edges
            bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
            
            # Create the histogram as a 3D bar plot
            ax.bar(bin_centers, hist, zs=offset_gap * i, zdir='y', alpha=0.8, width=hist_width, label=feature_name)
        
        # Set labels for the axes
        ax.set_xlabel('Feature Values')
        ax.set_ylabel('Feature Index (Separated)')
        ax.set_zlabel('Frequency')
        
        # Set the title and legend
        ax.set_title("3D Histogram View of CSV Dataset Features (Excluding Class)")
        ax.legend()
        
        fig.canvas.draw_idle()
    
    # Initial plot
    update_plot(initial_bins)
    
    # Add slider for bin size control
    slider_ax = fig.add_axes([0.2, 0.02, 0.6, 0.03])
    slider = Slider(slider_ax, 'Bins', 5, 50, valinit=initial_bins, valstep=1)
    slider.on_changed(update_plot)
    
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
