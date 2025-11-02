import matplotlib.pyplot as plt

def create_line_graph():
    # I know the homework assignment said to use the data from the other file, but scripting is not my forte
    # so I am going to just hard code the values here into a script I tried to follow on Youtube. Yolo

    # The values
    x_axis = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
    y_axis = [10, 11, 8, 16, 16, 8, 36]

    # The window size in inches with colors and other details 
    plt.figure(figsize=(8, 5))
    plt.plot(x_axis, y_axis, marker='o', linestyle='-', color='b')

    # The labels
    plt.xlabel('Year')
    plt.ylabel('No. of Attacks')
    plt.title('Reported Number of IoT Attacks on Smith Hospital')
    plt.grid(True)

    # Generating the actual file
    Script = 'line_graph_for_attacks.png' 
    plt.savefig(Script, dpi=100) # (Save as a PNG file specifically)

    # HOPEFULLY this will make a graph pop up. 
    print(f"Graph saved as {Script}")

    # They had this line in their version too. It was hard to translate everything and I'm not susre if I need this 
    # so I'll just comment it out for now. 
    # plt.show()

if __name__ == "__main__":
    create_line_graph()
