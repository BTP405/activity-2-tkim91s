import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Step 1: Read Snowfall Data from the File
    snowfall_data = []
    with open(t, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file if line.strip()]

    # Step 2: Determine Ranges and Counts
    ranges = [i for i in range(0, max(snowfall_data) + 11, 10)]  # Adjusted range for the last bin
    counts = [snowfall_data.count(x) for x in ranges[:-1]]

    # Step 3: Plotting the Bar Chart
    plt.bar(ranges[:-1], counts, width=10, edgecolor='black')
    plt.xlabel('Snowfall Range (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Distribution')
    plt.xticks(ranges[:-1])  # Set x-axis ticks to match the range boundaries
    plt.show()


graphSnowfall("snowfall_data.txt")

