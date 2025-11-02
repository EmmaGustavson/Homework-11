import matplotlib.pyplot as plt

def create_line_graph():
    # Define your five data points (X and Y coordinates)
    x_points = [1, 2, 3, 4, 5]
    y_points = [2, 5, 3, 6, 4]

    # Create the plot
    plt.figure(figsize=(8, 5)) # Optional: Adjust figure size
    plt.plot(x_points, y_points, marker='o', linestyle='-', color='b')

    # Add labels and title
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.title('Line Graph of Five Points')
    plt.grid(True) # Optional: Add a grid

    # Save the figure to a file
    file_name = 'line_graph.png'
    plt.savefig(file_name, dpi=100) # Save as PNG with 100 DPI
    
    print(f"Graph saved as {file_name}")

    # Optional: Display the graph (if running locally and have a display environment)
    # plt.show()

if __name__ == "__main__":
    create_line_graph()
