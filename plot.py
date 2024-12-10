import matplotlib.pyplot as plt
import csv
from collections import Counter

def plot_results(csv_file):
    percentage_of_moves_used_random, board_size_random = [], []
    percentage_of_moves_used_heuristic, board_size_heuristic = [], []
    
    with open("Results/" + csv_file + "_random.csv", 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            try:
                percentage_of_moves_used_random.append(float(row[0]) / float(row[1]) * 100)
                board_size_random.append(int(row[1]) / 35)
            except ValueError:
                continue

    with open("Results/" + csv_file + "_heuristic.csv", 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            try:
                percentage_of_moves_used_heuristic.append(float(row[0]) / float(row[1]) * 100)
                board_size_heuristic.append(int(row[1]) / 35)
            except ValueError:
                continue

    plt.scatter(board_size_random, percentage_of_moves_used_random, color='blue', label='Random Strategy')
    plt.scatter(board_size_heuristic, percentage_of_moves_used_heuristic, color='red', label='Heuristic Strategy')
    
    plt.ylim(0, 100)
    plt.title('Percentage of Moves Used over Board Size')
    plt.xlabel('Board Size')
    plt.ylabel('Percentage of Moves Used')

    plt.legend(loc='best', fontsize=10, frameon=True, shadow=True, title="Legend")
    plt.grid(True)
    plt.show()

def distribution_histogram(csv_file):
    def process_data(file_suffix):
        percentages = []
        with open(f"Results/{csv_file}_{file_suffix}.csv", 'r') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            for row in data:
                try:
                    moves_used = float(row[0])
                    move_limit = float(row[1])
                    percentages.append((moves_used, move_limit))
                except ValueError:
                    continue
        return percentages

    def calculate_bins(data, thresholds):
        total_runs = len(data)
        bins = {}
        for threshold in thresholds:
            count = sum((moves / limit) < (threshold / 100.0) for moves, limit in data)
            bins[f"<{threshold}%"] = (count / total_runs) * 100
        return bins

    # Process data
    random_data = process_data("random")
    heuristic_data = process_data("heuristic")
    
    # Define thresholds
    thresholds = list(range(100, 0, -10))  # [100, 90, 80, ..., 10]
    
    # Calculate bins
    random_bins = calculate_bins(random_data, thresholds)
    heuristic_bins = calculate_bins(heuristic_data, thresholds)
    
    # Bar chart data
    categories = list(random_bins.keys())
    random_values = list(random_bins.values())
    heuristic_values = list(heuristic_bins.values())
    
    x = range(len(categories))
    
    # Plot the histogram
    bar_width = 0.35
    plt.bar(x, random_values, width=bar_width, color='blue', label='Random Strategy')
    plt.bar([i + bar_width for i in x], heuristic_values, width=bar_width, color='red', label='Heuristic Strategy')
    
    # Customization
    plt.xticks([i + bar_width / 2 for i in x], categories, rotation=45)
    plt.ylim(60, 100)
    plt.title("Success Rates Under (%) of Move Limit")
    plt.xlabel("Tresholds")
    plt.ylabel("Percentage (%) of Successful Runs")
    plt.legend(loc='lower left', fontsize=10, frameon=True, shadow=True, title="Legend")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def result_distribution(csv_file):
    percentage_distribution_random = []
    percentage_distribution_heuristic = []
    
    # Process Random Strategy data
    with open("Results/" + csv_file + "_random.csv", 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            try:
                percentage = round(float(row[0]) / float(row[1]) * 100, 2)
                percentage_distribution_random.append(percentage)
            except ValueError:
                continue
    
    # Process Heuristic Strategy data
    with open("Results/" + csv_file + "_heuristic.csv", 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            try:
                percentage = round(float(row[0]) / float(row[1]) * 100, 2)
                percentage_distribution_heuristic.append(percentage)
            except ValueError:
                continue

    # Count occurrences of each percentage
    random_counts = Counter(percentage_distribution_random)
    heuristic_counts = Counter(percentage_distribution_heuristic)
    
    # Extract data for scatter plot
    random_percentages, random_occurrences = zip(*sorted(random_counts.items()))
    heuristic_percentages, heuristic_occurrences = zip(*sorted(heuristic_counts.items()))

    # Plot the distribution
    plt.scatter(random_percentages, random_occurrences, color='blue', label='Random Strategy')
    plt.scatter(heuristic_percentages, heuristic_occurrences, color='red', label='Heuristic Strategy')

    plt.title('Distribution of Frequency')
    plt.xlabel('Percentage of Moves Used')
    plt.ylabel('Frequency')
    plt.legend(loc='best', fontsize=10, frameon=True, shadow=True, title="Legend")
    plt.grid(True)
    plt.show()

result_distribution("stats")